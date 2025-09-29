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

    def get_url_params(self, context: dict, next_page_token: str) -> dict:
        """Return a dictionary or string of URL query parameters.

        Args:
            context: Stream partition or context dictionary.
            next_page_token: Token, page number or any request argument to request the
                next page of data.

        Returns:
            Dictionary or encoded string with URL query parameters to use in the
                request.
        """
        return {
            "includeSessionIds": True,
            "sortBy": "updated_at",
            "sortOrder": "asc",
            "limit": self.page_size,
            "page": next_page_token,
            "updatedAfter": self.get_starting_timestamp(context),
        }

    def get_new_paginator(self) -> BasePageNumberPaginator:
        """Get a fresh paginator for this API endpoint.

        Returns:
            A paginator instance.
        """
        return BasePageNumberPaginator(1)


class SessionsStream(OpenCXStream):
    name = "sessions"
    path = "/chat/sessions"
    records_jsonpath = "$.items[*]"
    schema = sessions_schema

    def get_url_params(self, context: dict, next_page_token: str) -> dict:
        """Return a dictionary or string of URL query parameters.

        Args:
            context: Stream partition or context dictionary.
            next_page_token: Token, page number or any request argument to request the
                next page of data.

        Returns:
            Dictionary or encoded string with URL query parameters to use in the
                request.
        """
        return {
            "cursor": next_page_token,
            "updated_after": self.get_starting_timestamp(context),
        }

    def get_new_paginator(self) -> JSONPathPaginator:
        """Get a fresh paginator for this API endpoint.

        Returns:
            A paginator instance.
        """
        return JSONPathPaginator(jsonpath="$.next")
