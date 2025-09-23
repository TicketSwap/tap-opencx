"""Tests standard tap features using the built-in SDK tests library."""

import datetime
import os

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_opencx.tap import TapOpenCX

SAMPLE_CONFIG = {
    "start_date": (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=12)).isoformat(),
    "access_token": os.getenv("TAP_OPENCX_ACCESS_TOKEN"),
}

TEST_SUITE_CONFIG = SuiteConfig(max_records_limit=100, ignore_no_records=True)


# Run standard built-in tap tests from the SDK:
TestTapOpenCX = get_tap_test_class(
    tap_class=TapOpenCX,
    config=SAMPLE_CONFIG,
    suite_config=TEST_SUITE_CONFIG,
)
