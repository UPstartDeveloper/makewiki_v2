from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page


# Create your tests here.
class WikiTestCase(TestCase):
    def test_true_is_true(self):
        '''Canary test to ensure the tests are able to run. Returns True.'''
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Page. """
        # Author is a required field in our model.
        # Create a user for this test and save it to the test database.
        user = User()
        user.save()

        # Create and save a new page to the test database.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()

        # Make sure the slug that was generated in Page.save()
        # matches what we think it should be.
        self.assertEqual(page.slug, "my-test-page")
