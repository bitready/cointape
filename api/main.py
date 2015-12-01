# requests
import requests

# settings
from django.conf import settings

class cointape_api_request(object):
    ''' Abstract Cointape API Request Class '''
    def request(self):
        response = requests.get(self.query_url)

        try:
            if getattr(settings, 'VIEW_API_REQUESTS', False):
                print '+++++'
                print self.query_url
                print '+++++'
                print '-----'
                try:
                    print response.json()
                except:
                    print response
                print '-----'

            return response.json()
        except:
            return False
