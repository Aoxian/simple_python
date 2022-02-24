import unittest

from src.simple_python import SimplePython

class SimplePythonTestCase(unittest.TestCase):

    def test_hello_world(self):
        subject = SimplePython()
        self.assertEqual(subject.hello_world(), "Hello, World!")
