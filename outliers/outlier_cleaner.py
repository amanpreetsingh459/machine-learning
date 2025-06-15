#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for pred, nw, age in zip(predictions, net_worths, ages):
      error = pred-nw
      cleaned_data.append((age, nw, error))

    print(cleaned_data)
    cleaned_data.sort(key=lambda x:(x[2], x[1]))
    data.sort(key=lambda x: (x[2], x[1]))
    data_length = len(cleaned_data)
    elements_to_discard = int(data_length*0.90)
    cleaned_data = cleaned_data[:elements_to_discard]
    
    return cleaned_data

