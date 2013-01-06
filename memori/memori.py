try:
    import json
except ImportError:
    import simplejson as json

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


class MemoriAPI(object):
    def __init__(self, token):
        self.token = token

    def photos(self):
        req = urllib2.Request(API_URL + '/v1/photo/?format=json')
        req.add_header('AUTHORIZATION', 'Bearer %s' % self.token)
        try:
            resp = urllib2.urlopen(req)
            return json.loads(resp.read(), object_hook=_obj_hook)
        except urllib2.HTTPError, e:
            print e


if __name__=='__main__':
    api = MemoriAPI('7b262d6bd5')
    photos = api.photos()
    import pdb
    pdb.set_trace()
