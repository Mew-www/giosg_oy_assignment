from django.test import SimpleTestCase
import json
import os


class InterfaceTests(SimpleTestCase):
    """
    Interface tests to validate output formats of APIs.

    REQUIRES envvar "GI_ASSIGNMENT_TEST_API_TOKEN".

    REMINDER: When using headers in tests, remember to pass in the already-HTTP_-prefixed (and underscored) version.
    """
    def test_total_v1_interface(self):
        response = self.client.get(
            '/reporting/v1/total/from-2017-05-01/to-2017-05-15',
            follow=True,
            **{'HTTP_X_GI_TOKEN': os.environ['GI_ASSIGNMENT_TEST_API_TOKEN']}
        )
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            json.loads(response.content).keys(),
            ['total_conversation_count', 'total_user_message_count', 'total_visitor_message_count']
        )

    def test_daily_v1_interface(self):
        response = self.client.get(
            '/reporting/v1/daily/from-2017-05-01/to-2017-05-15',
            follow=True,
            **{'HTTP_X_GI_TOKEN': os.environ['GI_ASSIGNMENT_TEST_API_TOKEN']}
        )
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            json.loads(response.content).keys(),
            ['by_date', 'paginated', 'current_page', 'max_page']
        )
