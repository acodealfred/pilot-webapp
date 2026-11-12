"""Binds the API scenario of PIL-3. Page scenarios are in tests/e2e."""

from pytest_bdd import parsers, scenario, when


@scenario("PIL-3/feature-requests.feature", "Request with an unknown category is rejected by the API")
def test_unknown_category_rejected():
    pass


@when(parsers.parse('I post a feature request with title "{title}" and category "{category}"'))
def post_request(client, context, title, category):
    context["response"] = client.post(
        "/api/feature-requests", json={"title": title, "category": category}
    )
