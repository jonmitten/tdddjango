from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# Can we resolve the URL for the root of the site to a
# particular view function we've made?

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

# Can we make this view function return some HTML which will get the 
# functional test to pass?

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do List</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))