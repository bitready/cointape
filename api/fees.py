# api requests
from cointape.api.main import cointape_api_request

# settings
from django.conf import settings

class fee_analysis(cointape_api_request):
    ''' Cointape Fee Overview '''
    def __init__(self):
        self.query_url = settings.COINTAPE_API_URL + 'fees/list'

class suggested_fees(cointape_api_request):
    ''' Cointape Suggested Fees '''
    def __init__(self):
        self.query_url = settings.COINTAPE_API_URL + 'fees/recommended'
