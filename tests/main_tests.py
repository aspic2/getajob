import unittest
import main


class TestMain(unittest.TestCase):

    def test_main(self):
        pass

    def test_valid_word(self):
        self.assertTrue(main.valid_word("Fireman"))
        self.assertFalse(main.valid_word("!Fire"))
        self.assertTrue(main.valid_word("F!re"))
        self.assertTrue(main.valid_word("Fire."))


