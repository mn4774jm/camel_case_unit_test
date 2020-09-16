
import camel_case
from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camel_case.camelCase_convert('Hello World'))
        self.assertEqual('', camel_case.camelCase_convert(''))
        self.assertEqual('helloWorld', camel_case.camelCase_convert('    hello     world'))
        self.assertEqual('helloWorld', camel_case.camelCase_convert('HELLO WORLD'))
        self.assertEqual('helloWorld', camel_case.camelCase_convert('Hello World!'))
        self.assertEqual('helloWorld', camel_case.camelCase_convert('$$$$$$$HellO WORLD!!!!!!'))







