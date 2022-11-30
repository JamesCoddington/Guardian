import unittest
from unittest.mock import patch, MagicMock, Mock

from startup import Guardian


class TestStartup(unittest.TestCase):
  guardian = Guardian()

  def test_user_input_yes(self):
    self.guardian.get_input = MagicMock(return_value = "y")
    self.guardian.monitor =  Mock()
    self.guardian.user_input()
    self.guardian.monitor.assert_called()

  def test_user_input_invalid_response(self):
    self.guardian.get_input = MagicMock(side_effect = ["NO", "n"])
    self.assertEqual(self.guardian.user_input(), None)
    
  def test_user_input_no(self):
    self.guardian.get_input = MagicMock(return_value = "n")
    self.assertEqual(self.guardian.user_input(), "Exiting the program")
  

if __name__ == "__main__":
  unittest.main()