from django.conf import settings
from django.http import HttpResponseServerError
from django.utils.deprecation import MiddlewareMixin


class AdministMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        ip = request.META['REMOTE_ADDR']

        if ip not in settings.ADMINIST_ALLOWED_IP:
            return HttpResponseServerError()
