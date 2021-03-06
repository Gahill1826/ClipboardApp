import os
import json
import re
from time_utils import TimeUtils
from multiprocessing import Lock
from config import config
from event_hashes import EventHashes
from event import EventManager
import requests

class AggregatorBase:
    # This class includes functionality that should be shared by spiders and API-based classes

    def __init__(self, organization, base_url, start_date, end_date, date_format, request_date_format = None):
        self.organization = organization
        # date_format is the string that specifies the date style of the target website
        if request_date_format == None:
            request_date_format = date_format

        self.date_format = date_format
        self.time_utils = TimeUtils(date_format)
        self.base_url = base_url
        self.identifier = re.sub(r'\W', '', base_url)
        self.event_manager = EventManager()
        
        request_format_utils = TimeUtils('%m-%d-%Y')
        # When this is running for multiple days, validating if the date is in the past causes issues
        self.start_date = request_format_utils.convert_date_format(start_date, request_date_format, validate_past=False)
        self.end_date = request_format_utils.convert_date_format(end_date, request_date_format, validate_past=False)
        self.start_timestamp = request_format_utils.min_timestamp_for_day(start_date)
        self.end_timestamp = request_format_utils.max_timestamp_for_day(end_date)