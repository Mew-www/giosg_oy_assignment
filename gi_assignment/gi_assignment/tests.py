from django.test import SimpleTestCase
from django.shortcuts import render_to_response


class GlobalTests(SimpleTestCase):
    """
    Global tests for generic cases e.g. template existence.
    """
    def test_http_404_template_exists(self):
        render_to_response('404.html')

    def test_http_500_template_exists(self):
        render_to_response('50x.html')
