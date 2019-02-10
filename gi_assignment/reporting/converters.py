from datetime import datetime


class DateConverter:
    """
    Accepts format YYYY-MM-DD, checks via datetime (invalid -> expect getting http404).
    converts to datetime -object
    """
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")


class PageConverter:
    """
    Accepts format page-1, page-2, page-10, etc. Not "page-0" though.
    converts to integer (page_num)
    """
    regex = 'page-[1-9]{1}[0-9]*'

    def to_python(self, value):
        return int(value.split('-')[1])

    def to_url(self, value):
        return 'page-{}'.format(value)
