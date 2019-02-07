from datetime import datetime


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value.strftime("%Y-%m-%d")


class PageConverter:
    regex = 'page-[1-9]{1}[0-9]*'  # page-1, page-2, etc.

    def to_python(self, value):
        return int(value.split('-')[1])

    def to_url(self, value):
        return 'page-{}'.format(value)
