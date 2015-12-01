# api
from cointape.api.fees import fee_analysis

# references
from cointape import references

def get_fees():
    fee_analysis = get_fee_analysis()
    if fee_analysis:
        chosen_fee_rate = choose_fee(fee_analysis)
        if fee_rate:
            print 'win', chosen_fee_rate
        else:
            print 'fail'
    else:
        ''' database fees '''
        print 'fail'
        pass

def get_fee_analysis():
    ''' Definition: Query API for suggested fees.
        Returns: list(Dict(fee_analysis)) OR None
    '''
    fees = fee_analysis().request()
    if fees and fees.get('fees', False) and type(fees['fees']) is list:
        success = True
        try:
            for fee_breakdown in fees['fees']:
                if not all(type(fee_breakdown.get(key, False)) is int \
                   for key in references.expected_keys):
                    success = False
                    break
            return fees['fees'] if success else None
        except:
            return None
    else:
        return None

def choose_fee(fee_analysis):
    ''' Definition: Choose fee to be used from fee analysis returned by API.
        Parameters: list(Dict(fee_analysis))
        Returns: int(chosen_fee_rate) OR None
    '''
    fee_analysis = sorted(fee_analysis, key=lambda k: k[references.fee_sort])
    for fee_breakdown in fee_analysis:
        if all(fee_breakdown[key] <= limit \
           for key, limit in references.fee_preferences.iteritems()):
            return fee_breakdown[references.fee_choice]
    return None

def calculate_tx_size(inputs, outputs):
    ''' Definition: Calculate the size of the transaction (in bytes) to be sent.
        Parameters: int(inputs), int(outputs)
        Returns: int(tx_size)
        NOTES: Solution based on this post on StackExchange.
         http://bitcoin.stackexchange.com/questions/1195/how-to-calculate-transaction-size-before-sending#answers-header
     '''
