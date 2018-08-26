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

def calc_minmax(value):
    min_val = 2
    max_val = 0
    min_ind = 0
    max_ind = 0
    for i in range(0, len(value)):
        if value[i] > max_val:
            max_val = value[i]
            max_ind = i
        
        if value[i] < min_val:
            min_val = value[i]
            min_ind = i
    min_info = (min_val, min_ind)
    max_info = (max_val, max_ind)
    return min_info, max_info

def weight_batch_calc_desc(input_array_title, input_array_desc, weights):
    for i in range(0, len(input_array_desc)):
        if not input_array_desc[i]:
            input_array_desc[i] = input_array_title[i]
    values = batch_calc(input_array_desc)
    min_info, max_info = calc_minmax(values)
    sum_weighted = 0
    sum_weights = 0
    for i in range(0, len(values)):
        sum_weighted += values[i]*weights[i][0]
        sum_weights += weights[i][0]
    mean = sum_weighted/sum_weights
    return mean, min_info, max_info

def batch_relevance(input_array_title, input_array_desc, input_str):
    for i in range(0, len(input_array_desc)):
        if not input_array_desc[i]:
            input_array_desc[i] = input_array_title[i]
    return indicoio.relevance(input_array_desc, [input_str])