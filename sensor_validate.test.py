import unittest
import sensor_validate

# Limit specification of battery Parameters
soc_limit = 0.05
current_limit = 0.1

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soc_jumps(self):
    
    self.assertFalse(
      sensor_validate.check_if_length_is_not_none_and_validate_reading([0.0, 0.01, 0.5, 0.51],soc_limit)
    )
  
  def test_reports_error_when_current_jumps(self):
    
    self.assertFalse(
      sensor_validate.check_if_length_is_not_none_and_validate_reading([0.03, 0.03, 0.03, 0.33],current_limit)
    )

if __name__ == "__main__":
  unittest.main()
