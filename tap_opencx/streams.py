"""Stream type classes for tap-opencx."""

from __future__ import annotations
from singer_sdk.pagination import BasePageNumberPaginator, JSONPathPaginator

from tap_opencx.client import OpenCXStream
from tap_opencx.schemas import (
    insights_schema,
    sessions_schema,
)

class InsightsStream(OpenCXStream):
    name = "insights"
    path = "/insights"
    records_jsonpath = "$.data[*]"
    schema = insights_schema
    page_size = 100

    def get_url_params(self, context, next_page_token):
        params = {
            "includeSessionIds": True,
            "sortBy": "updated_at",
            "sortOrder": "asc",
            "limit": self.page_size,
            "page": next_page_token,
            "updatedAfter": self.get_starting_timestamp(context),
        }
        return params

    def get_new_paginator(self):
        return BasePageNumberPaginator(1)

class SessionsStream(OpenCXStream):
    name = "sessions"
    path = "/chat/sessions"
    records_jsonpath = "$.items[*]"
    schema = sessions_schema

    def get_url_params(self, context, next_page_token):
        params = {
            "cursor": next_page_token,
            "updated_after": self.get_starting_timestamp(context),
        }
        return params

    def get_new_paginator(self):
        return JSONPathPaginator(jsonpath="$.next")
