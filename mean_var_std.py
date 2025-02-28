import numpy as np

def calculate(list):

  if len(list) < 9:
    return print('List must contain nine numbers.') 
  else:
    array = np.array([list[0:3],list[3:6],list[6:9]]) 
    calculations = {} 

    #mean
    media_horiz = array.mean(axis=0).tolist()
    media_vert = array.mean(axis=1).tolist()
    media_total = array.mean()
    calculations['mean'] = [media_horiz, media_vert, media_total]

    #variance
    var_horiz = array.var(axis=0).tolist()
    var_vert = array.var(axis=1).tolist()
    var_total = array.var()
    calculations['variance'] = [var_horiz, var_vert, var_total]  

    #standard deviation
    sd_horiz = array.std(axis=0).tolist()
    sd_vert = array.std(axis=1).tolist()
    sd_total = array.std()
    calculations['standard deviation'] = [sd_horiz, sd_vert, sd_total]  

    #max
    max_horiz = array.max(axis=0).tolist()
    max_vert = array.max(axis=1).tolist()
    max_total = array.max()
    calculations['max'] = [max_horiz, max_vert, max_total]  

    #min
    min_horiz = array.min(axis=0).tolist()
    min_vert = array.min(axis=1).tolist()
    min_total = array.min()
    calculations['min'] = [min_horiz, min_vert, min_total]  

    #sum
    sum_horiz = array.sum(axis=0).tolist()
    sum_vert = array.sum(axis=1).tolist()
    sum_total = array.sum()
    calculations['sum'] = [sum_horiz, sum_vert, sum_total]    


    return print(calculations)
