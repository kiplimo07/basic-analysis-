import numpy as np
try:
 def calculate(input):
     arr = np.array(input).reshape(3,3)
     cal = dict()
     cal['Mean'] = [arr.mean(0).tolist(),arr.mean(1).tolist(),arr.mean()]
     cal['variance'] = [arr.var(0).tolist(),arr.var(1).tolist(),arr.var()]
     cal['standard deviation'] = [arr.std(0).tolist(),arr.std(1).tolist(),arr.std()]
     cal['max'] = [arr.max(0).tolist(),arr.max(1).tolist(),arr.max()]
     cal['Min'] = [arr.min(0).tolist(),arr.min(1).tolist(),arr.min()]
     cal['sum'] = [arr.sum(0).tolist(),arr.sum(1).tolist(),arr.sum()]
     return cal;
except:
  if len(input)!=9:
    print("value error")
    
print(calculate([0,1,2,3,4,5,6,7,8]))