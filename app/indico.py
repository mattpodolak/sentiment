import indicoio 

def single_calc(input_string):
    return indicoio.sentiment_hq(input_string)

def batch_calc(input_array):
    return indicoio.sentiment_hq(input_array)

def avg_batch_calc(input_array):
    values = batch_calc(input_array)
    mean = sum(values)/len(values)
    return mean

def weight_batch_calc(input_array, weights):
    values = batch_calc(input_array)
    sum_weighted = 0
    sum_weights = 0
    for i in range(0, len(values)):
        sum_weighted += values[i]*weights[i][0]
        sum_weights += weights[i][0]
    mean = sum_weighted/sum_weights
    return mean

def batch_relevance(input_array_title, input_array_desc, input_str):
    for i in range(0, len(input_array_desc)):
        if not input_array_desc[i]:
            input_array_desc[i] = input_array_title[i]
    return indicoio.relevance(input_array_desc, [input_str])