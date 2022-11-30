import unittest
import json
import csv
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

  def test_user_prompt_yes(self):
    status = {"whitelist": [], "blacklist": []}
    application_name = "test_yes"
    application_path = "test_yes"
    self.guardian.get_input = MagicMock(return_value = "y")
    self.guardian.user_prompt(status, application_name, application_path)
    self.assertEqual(status["whitelist"], [application_path])

  def test_user_prompt_no(self):
    status = {"whitelist": [], "blacklist": []}
    application_name = "test_no"
    application_path = "test_no"
    self.guardian.get_input = MagicMock(return_value = "n")
    self.guardian.output_log = MagicMock()
    csv.writer = MagicMock()
    csv.writer.writerow = MagicMock()
    self.guardian.user_prompt(status, application_name, application_path)
    self.assertEqual(status["blacklist"], [application_path])

  def test_check_csv(self):
    csv.writer = MagicMock()
    csv.writer.writerow = MagicMock()
    self.guardian.check_csv()

if __name__ == "__main__":
  unittest.main()