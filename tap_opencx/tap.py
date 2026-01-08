"""OpenCX tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_opencx import streams


class TapOpenCX(Tap):
    """OpenCX tap class."""

    name = "tap-opencx"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The key to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync, in ISO 8601 timestamp format",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.OpenCXStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.SessionsStream(self),
        ]


if __name__ == "__main__":
    TapOpenCX.cli()
