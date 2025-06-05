from datetime import datetime
import logging
from datetime import datetime, time
from django.http import HttpResponseForbidden
from datetime import datetime, timedelta
from django.http import JsonResponse
from collections import defaultdict
import threading
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

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Stockage des requêtes par IP
        self.request_log = defaultdict(list)
        self.lock = threading.Lock()  # Pour les accès concurrents

    def __call__(self, request):
        # Applique uniquement pour les POST vers les messages
        if request.method == "POST" and request.path.startswith("/api/messages"):
            ip = self.get_client_ip(request)
            now = datetime.now()

            with self.lock:
                # Nettoyer les vieilles entrées (> 1 minute)
                self.request_log[ip] = [t for t in self.request_log[ip] if now - t < timedelta(minutes=1)]

                if len(self.request_log[ip]) >= 5:
                    return JsonResponse(
                        {"error": "Rate limit exceeded. Max 5 messages per minute."},
                        status=429
                    )

                self.request_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip