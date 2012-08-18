from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf


class LoginFormMiddleware(object):
    def process_request(self, request):
        c = {}
        c.update(csrf(request))
        # attach the form to the request so it can be accessed within the templates
        request.csrf = c['csrf_token']