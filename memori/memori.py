try:
    import json
except ImportError:
    import simplejson as json

import time
import urllib2

DEBUG = False

if DEBUG:
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)

API_URL = 'http://192.168.1.194'
# API_URL = 'http://api.memori.cn'


class JsonObject(dict):
    '''
    general json object that can bind any fields but also act as a dict.
    '''
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


def _obj_hook(pairs):
    '''
    convert json object to python object.
    '''
    o = JsonObject()
    for k, v in pairs.iteritems():
        o[str(k)] = v
    return o


_CONTENT_TYPES = { '.png': 'image/png', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.jpe': 'image/jpeg' }

def _guess_content_type(ext):
    return _CONTENT_TYPES.get(ext, 'application/octet-stream')


def _encode_multipart(**kw):
    '''
    Build a multipart/form-data body with generated random boundary.
    '''
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    for k, v in kw.iteritems():
        data.append('--%s' % boundary)
        if hasattr(v, 'read'):
            # file-like object:
            ext = ''
            filename = getattr(v, 'name', '')
            n = filename.rfind('.')
            if n != (-1):
                ext = filename[n:].lower()
            content = v.read()
            data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (k, filename))
            data.append('Content-Length: %d' % len(content))
            data.append('Content-Type: %s\r\n' % _guess_content_type(ext))
            data.append(content)
        else:
            data.append('Content-Disposition: form-data; name="%s"\r\n' % k)
            data.append(v.encode('utf-8') if isinstance(v, unicode) else v)
    data.append('--%s--\r\n' % boundary)
    return '\r\n'.join(data), boundary


def _encode_params(**kw):
    '''
    Encode parameters.
    '''
    args = []
    for k, v in kw.iteritems():
        qv = v.encode('utf-8') if isinstance(v, unicode) else str(v)
        args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)


class APIRequest(object):
    def __init__(self, method, url, token, data=None, files=None):
        self.req = urllib2.Request(API_URL + url)
        self.req.get_method = lambda : method
        self.req.add_header('AUTHORIZATION', 'Bearer %s' % token)
        self.data = data
        self.files = files

    def build_http_request(self):
        if self.req.get_method() == 'GET':
            pass
        if self.req.get_method() == 'POST':
            if len(self.files) > 0:
                params, boundary = _encode_multipart(**self.files)
                self.req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
            else:
                params = _encode_params(**self.data)
            self.req.add_data(params)
        return self.req

class MemoriAPI(object):
    def __init__(self, token):
        self.token = token

    def execute(self, request):
        resp = urllib2.urlopen(request.build_http_request())
        return json.loads(resp.read(), object_hook=_obj_hook)
            
    def photos(self):
        req = APIRequest('GET', '/v1/photo/', self.token)
        try:
            return self.execute(req)
        except urllib2.HTTPError, e:
            print e

    def photo__upload(self, photo, shotted_at=None, location=None, voice=None,
                      memori=None, local_key=None):
        values = {'photo': open(photo)}
        if shotted_at is not None:
            values['shotted_at'] = shotted_at
        req = APIRequest('POST', '/v1/photo/upload/', self.token, files=values)
        try:
            return self.execute(req)
        except urllib2.HTTPError, e:
            print e        


if __name__=='__main__':
    api = MemoriAPI('7b262d6bd5')
    photos = api.photos()
    print photos.meta.total_count
    print api.photo__upload('./upload.jpg', shotted_at='2012-08-09 14:50:37')
