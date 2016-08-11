# coding: utf-8

from dateparser.calendars import CalendarBase
from dateparser.calendars.hijri_parser import hijri_parser


class HijriCalendar(CalendarBase):
    parser = hijri_parser
