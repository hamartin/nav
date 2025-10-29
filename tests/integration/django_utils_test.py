import logging

from django.test import RequestFactory, TestCase

from nav.django.utils import pp_request


_logger = logging.getLogger(__name__)


class TestPPRequest(TestCase):
    def test_pp_request_should_log_more_lines_than_there_are_attributes_in_request(
        self,
    ):
        r = RequestFactory()
        request = r.get('/')
        num_request_attributes = len(vars(request))
        with self.assertLogs(level=logging.DEBUG) as logs:
            pp_request(request, _logger.debug)
            self.assertTrue(len(logs.records) > num_request_attributes)

    def test_pp_request_should_log_nothing_for_nonexistent_attribute(self):
        r = RequestFactory()
        request = r.get('/')
        with self.assertRaises(AssertionError):
            with self.assertLogs():
                pp_request(request, _logger.debug, 'doesnotexist-nanana')

    def test_pp_request_should_log_one_line_for_content_type(self):
        r = RequestFactory()
        request = r.get('/')
        with self.assertLogs(level=logging.DEBUG) as logs:
            pp_request(request, _logger.debug, 'content_type')
            self.assertEqual(len(logs.records), 1)
