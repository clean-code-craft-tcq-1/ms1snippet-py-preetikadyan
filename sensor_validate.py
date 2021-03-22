
def  check_if_soc_or_charging_parameter_gives_noise(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_reading(values):
  #length = len(values)
  #if length != 0:  
      last_but_one_reading = len(values) - 1
      for i in range(last_but_one_reading):
          if(not check_if_soc_or_charging_parameter_gives_noise(values[i], values[i + 1], 0.05)):
              return False
      return True

