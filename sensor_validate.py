
def  check_if_given_parameter_produces_noise(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def check_if_length_is_not_none_and_validate_reading(values,limit):
    length = len(values)
    if length != 0:
       validate_reading(values,length - 1,limit)
  
def validate_reading(values, last_but_one_reading,limit):
      for i in range(last_but_one_reading):
          if(not check_if_given_parameter_produces_noise(values[i], values[i + 1], limit)):
              return False
      return True

