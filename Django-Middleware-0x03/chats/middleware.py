from datetime import datetime
import logging
from datetime import datetime, time
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure logging
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s',
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        start_time = time(18, 0)  # 18h00
        end_time = time(21, 0)    # 21h00

        if not (start_time <= now <= end_time):
            return HttpResponseForbidden("⛔ Access to the messaging app is only allowed between 6 PM and 9 PM.")

        response = self.get_response(request)
        return response

