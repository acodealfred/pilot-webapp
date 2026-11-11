"""Binds the API scenario of PIL-1. Page scenarios are in tests/e2e."""

from pytest_bdd import scenario


@scenario("PIL-1/about-version.feature", "Version endpoint reports the app version")
def test_version_endpoint():
    pass
