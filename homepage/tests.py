from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(3+3, 2)