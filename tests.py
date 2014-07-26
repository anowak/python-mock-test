import unittest
from mock import patch, Mock
from storage import Storage
# from models import Model

class StorageTestCase(unittest.TestCase):
  @patch('storage.Model')
  def test(self, model_class_mock):
    save_mock = Mock(return_value='mocked')
    model_class_mock.return_value.save = save_mock

    storage = Storage()
    result = storage.populate()
    self.assertEqual(save_mock.call_count, 1)
    self.assertEqual(result, 'mocked')

if __name__ == "__main__":
  unittest.main()
