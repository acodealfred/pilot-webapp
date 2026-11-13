"""Binds the API scenario of PIL-4. Page scenarios are in tests/e2e."""

from pytest_bdd import scenario


@scenario("PIL-4/search-feature-requests.feature", "API filters requests by search text")
def test_api_search():
    pass
