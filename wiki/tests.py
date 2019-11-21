from django.test import TestCase


# Create your tests here.
class WikiTestCase(TestCase):
    def test_true_is_true(self):
        '''Canary test to ensure the tests are able to run. Returns True.'''
        self.assertEqual(True, True)
