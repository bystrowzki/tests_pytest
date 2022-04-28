import unittest
from unittest import mock
from code2 import new_folder, get_folders_files_list


class TestCode(unittest.TestCase):

    def setUp(self):
        print('method setup')

    def tearDown(self):
        print('method teardown')

    def test_get_folders_files_list(self):
        self.assertEqual(get_folders_files_list()[0], 200)

    def test_new_folder(self):
        folder_name = 'test'
        with mock.patch('builtins.input', return_value=folder_name):
            self.assertEqual(new_folder(), 201)

    @unittest.expectedFailure
    def test_new_folder_fail(self):
        folder_name = 'test'
        with mock.patch('builtins.input', return_value=folder_name):
            self.assertEqual(new_folder(), 201)

    def test_new_folder_2(self):
        folder_name = 'folder5'
        with mock.patch('builtins.input', return_value=folder_name):
            new_folder()
            list = []
            for x in get_folders_files_list()[1]['_embedded']['items']:
                if folder_name == x['name']:
                    list.append(x['name'])
                    n = get_folders_files_list()[1]['_embedded']['items'].index(x)
                    print(n, list)
                    self.assertIn(list[0], get_folders_files_list()[1]['_embedded']['items'][n]['name'])
                else:
                    continue


if __name__ == '__main__':
    unittest.main()
