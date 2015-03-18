from django.http import HttpResponse
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from gevent.greenlet import Greenlet

class GameNamespace(BaseNamespace):
    def recv_message(self, message):
        self.emit("message",  message)

def socketio(request):
    retval = socketio_manage(request.environ,  {
            '': GameNamespace,
        }, request)
    return HttpResponse(retval)
