from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from wiki.models import Page
from django.utils import timezone
from django.urls import reverse
from wiki.views import PageCreate


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


class PageListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test",
                            author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: My Test Page>', '<Page: Another Test Page>'],
            ordered=False
        )


class PageDetailViewTests(TestCase):
    def test_detail_view_for_one_page(self):
        '''The detail view for a specific page loads with the Page's data.'''
        # data to simulate user experience of making a new Page
        user = User.objects.create()
        Page.objects.create(title="My Test Page", content="test", author=user)

        # issues GET request to the testing database
        response = self.client.get('/my-test-page')

        # test that the number of pages in the template is only one
        response_num = response.context['page']
        self.assertEqual(type(response_num), Page)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'My Test Page')


class PageCreateTests(TestCase):
    def setUp(self):
        """Instantiate RequestFactory and User objects to pass POST requests
           to the PageCreate view.

        """
        self.factory = RequestFactory()
        self.user = User.objects.create(username='Abdullah',
                                        email='abd@gmail.com',
                                        password="Abdullah's passwd")

    def test_getting_creation_form(self):
        '''Create form displays with fields to enter title and content.'''
        response = self.client.get(reverse('wiki:create_page_form'))
        self.assertIn(b'Title of your page.', response.content)
        self.assertIn(b'Write the content of your page here.',
                      response.content)

    def test_submit_create_form(self):
        '''A new page is created after the user submits the creation form.'''

        form_data = {
            'title': 'My Test Page',
            'content': 'This is a test page.'
        }

        post_request = self.factory.post('wiki:create_page_form', form_data)
        post_request.user = self.user
        response = PageCreate.as_view()(post_request)
        # test the view ends in a redirect to the details page
        self.assertEqual(response.status_code, 302)
        # test that the database contains the new Page
        page = Page.objects.last()
        self.assertEqual(page.title, 'My Test Page')
