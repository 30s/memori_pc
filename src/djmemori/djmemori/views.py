from datetime import datetime, timedelta

from django.http import HttpResponse

from djmemori.models import Photo


def event_generator(hours=1):
    delta = timedelta(hours=hours)
    photo_stream = Photo.objects.all().order_by('-date_taken')
    event = []
    for p in photo_stream:
        if len(event) == 0:
            event.append(p)
        elif event[-1].date_taken - p.date_taken > delta:
            yield event
            event = []
        else:
            event.append(p)

            
def events(request):
    out = []
    for i in event_generator():
        out.append('<h2>%s - %d</h2>' % (str(i[0].date_taken), len(i)))
        out.append('<ul>')
        for p in i:
            out.append('<li><a href="file://%s%s">%s</a></li>' % (p.root.path, p.path, p.path))
        out.append('</ul>')
    return HttpResponse(''.join(out))
