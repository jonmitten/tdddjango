from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Can we resolve the URL for the root of the site to a
# particular view function we've made?

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

# Can we make this view function return some HTML which will get the 
# functional test to pass?