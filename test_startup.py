import unittest
from unittest.mock import patch, MagicMock, Mock

from startup import Guardian


class TestStartup(unittest.TestCase):

  def test_user_input_yes(self):
    guardian = Guardian()
    guardian.get_input = MagicMock(return_value = "y")
    guardian.monitor =  Mock()
    guardian.user_input()
    guardian.monitor.assert_called()

  def test_user_input_invalid_response(self):
    guardian = Guardian()
    guardian.get_input = MagicMock(side_effect = ["NO", "n"])
    self.assertEqual(guardian.user_input(), None)
    
  def test_user_input_no(self):
    guardian = Guardian()
    guardian.get_input = MagicMock(return_value = "n")
    self.assertEqual(guardian.user_input(), "Exiting the program")
  



if __name__ == "__main__":
  unittest.main()