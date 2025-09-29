"""REST client handling, including OpenCXStream base class."""

from __future__ import annotations

import typing as th
from pathlib import Path

import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.streams import RESTStream

_Auth = th.Callable[[requests.PreparedRequest], requests.PreparedRequest]
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class OpenCXStream(RESTStream):
    """OpenCX stream class."""

    primary_keys: th.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://api.open.cx"

    @property
    def authenticator(self):
        """Return the authenticator."""
        return BearerTokenAuthenticator(token=self.config.get("access_token"))
