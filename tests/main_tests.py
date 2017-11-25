import unittest
import main
import string
import re



class TestMain(unittest.TestCase):

    def test_main(self):
        pass

    def test_valid_word(self):
        self.assertTrue(main.valid_word("Fireman"))
        self.assertFalse(main.valid_word("!Fire"))
        self.assertTrue(main.valid_word("F!re"))
        self.assertTrue(main.valid_word("Fire."))

    def test_re_match(self):
        w1 = "hello"
        w2 = "hello!"
        w3 = "don't worry about a t%ing."
        p = re.compile("^\W")
        m1 = p.search(w1)
        m2 = p.search(w2)
        m3 = p.search(w3)
        print(m3)
        counter = 0
        w3.split(" ")





if __name__ == '__main__':
    #unittest.main()
    TestMain.test_re_match()


