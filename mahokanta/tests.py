import unittest
import webtest

class FTest(unittest.TestCase):
    def _getTarget(self):
        from mahokanta.app import dump
        return webtest.TestApp(dump)

    def assertStartsWith(self, expect, actual):
        message = "{0} != {1}".format(actual[:len(expect)], expect)
        assert actual.startswith(expect), message

    def test_it(self):
        target = self._getTarget()
        result = target.get('/')
        self.assertStartsWith(b"GET / HTTP/1.0\r\nHost: localhost:80", 
                              result.body)
