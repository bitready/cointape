# api expected response
expected_keys = ['dayCount', 'memCount', 'minDelay',
                 'maxDelay', 'minMinutes', 'maxMinutes']

# fee choice options
fee_sort = 'minFee'
fee_preferences = {'maxDelay': 2, 'maxMinutes': 60, 'maxFee': 100} # note: only use 'max' stats
fee_choice = 'minFee' # minFee OR maxFee

# fallbacks (ie. bad api response)
default_fee = 70 # 2015-30-11: should process in 1 block
