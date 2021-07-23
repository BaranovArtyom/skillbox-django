import datetime
import time

class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        if self.count % 3 == 0 and self.count != 0:
            time.sleep(5)

        response = self.get_response(request)
        self.count += 1
        return response