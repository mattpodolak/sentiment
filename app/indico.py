import indicoio 

def single_calc(input_string):
    return indicoio.sentiment_hq(input_string)

def batch_calc(input_array):
    return indicoio.sentiment_hq(input_array)