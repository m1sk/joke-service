from starlette.middleware.base import BaseHTTPMiddleware
import datetime

class Logger(BaseHTTPMiddleware):
    def __init__(self, app, account_provider=None, dateformat=None):
        super().__init__(app)
        self.account_provider = account_provider
        self.dateformat = dateformat

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        account=None
        if self.account_provider:
            account = self.account_provider(request)
        now = datetime.datetime.now()
        print(
              now.strftime(self.dateformat) if self.dateformat else now, 
              account if account else 'UNAUTHORIZED', 
              request.client.host, 
              request.scope['endpoint'].__name__ if 'endpoint' in request.scope else 'NONE', 
              request.method, 
              response.status_code 
            )
        return response
