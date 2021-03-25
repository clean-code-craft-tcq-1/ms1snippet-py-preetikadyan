
def  check_if_given_parameter_produces_noise(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def check_if_length_is_not_none_and_validate_reading(values,limit,parameter_name):
    length = len(values)
    if length != 0:
       print("--------------Validate Reading for the Parameter ",parameter_name,"--------------")
       validate_reading(values,length - 1,limit)
    else:
       print("Length of the battery parameter ' ",parameter_name," ' is None!!! Cannot validate reading!!!")
  
def validate_reading(values, last_but_one_reading,limit):
      for i in range(last_but_one_reading):
          if(not check_if_given_parameter_produces_noise(values[i], values[i + 1], limit)):
              return False
      return True

