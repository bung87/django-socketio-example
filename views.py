from django.http import HttpResponse
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from django.forms.models import model_to_dict

clients={}

class GlobalNamespace(BaseNamespace):
    '''https://gevent-socketio.readthedocs.org/en/latest/_modules/socketio/namespace.html'''
    def initialize(self):
        '''If you override this method, you probably want to initialize
        the variables you're going to use in the events handled by this
        namespace, setup ACLs, etc..'''
        pass
    def recv_connect(self):
        """Called the first time a client connection is open on a
        Namespace. This *does not* fire on the global namespace."""
        if not clients.has_key(self.request.session.session_key):
            clients[self.request.session.session_key]=self
        pass
    def recv_message(self, message):
        self.emit("message",  message)
    def on_task(self,message):
        self.emit('task',dict(message=message))

def socketio(request):
    '''The request object is not required, 
    but will probably be useful to pass framework-specific things into your Socket and Namespace functions.
     It will simply be attached to the Socket and Namespace object (accessible through self.request in both cases), 
     and it is not accessed in any case by the gevent-socketio library.'''
    retval = socketio_manage(request.environ,  {
            '/gosun': GlobalNamespace,
        }, request)
    return HttpResponse(retval)
