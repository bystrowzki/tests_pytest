import pytest
from unittest import mock
from code import new_document, delete_document, list_of_docs, new_shelf, documents, directories


class TestCode:

    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    def test_list_of_docs(self):
        data = []
        for items in documents:
            for key in items.keys():
                data.append(items[key])
        assert list_of_docs(documents) == data

    def test_delete_doc(self):
        n = len(documents)
        with mock.patch('builtins.input', return_value='10006'):
            assert delete_document(documents, directories) == n-1

    def test_delete_doc_fail(self):
        n = len(documents)
        with mock.patch('builtins.input', return_value='10005'):
            assert not delete_document(documents, directories) == n-1

    def test_new_doc(self):
        n = len(documents)
        with mock.patch('builtins.input', return_value='145'):
            with mock.patch('builtins.input', return_value='name'):
                with mock.patch('builtins.input', return_value='doc'):
                    with mock.patch('builtins.input', return_value='x'):
                        if new_document(documents, directories) == KeyError:
                            with mock.patch('builtins.input', return_value='1'):
                                assert new_document(documents, directories) == n+1
                        else:
                            assert new_document(documents, directories) == n+1

    def test_new_doc_fail(self):
        with mock.patch('builtins.input', return_value='145'):
            with mock.patch('builtins.input', return_value='name'):
                with mock.patch('builtins.input', return_value='doc'):
                    with mock.patch('builtins.input', return_value='x'):
                        if new_document(documents, directories) == KeyError:
                            with mock.patch('builtins.input', return_value='x'):
                                assert new_document(documents, directories) == KeyError

    def test_new_shelf(self):
        n = len(directories)
        with mock.patch('builtins.input', return_value='4'):
            assert new_shelf(directories) == n + 1

    def test_new_shelf_fail(self):
        with mock.patch('builtins.input', return_value='1'):
            assert new_shelf(directories) == KeyError
