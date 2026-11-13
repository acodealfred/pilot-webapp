"""Binds the page scenarios of PIL-4 (need a browser)."""

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenario, then, when

FEATURE = "PIL-4/search-feature-requests.feature"


@pytest.mark.e2e
@scenario(FEATURE, "Search shows only matching requests")
def test_search_matches():
    pass


@pytest.mark.e2e
@scenario(FEATURE, "Search with no match shows a message")
def test_search_no_match():
    pass


@pytest.mark.e2e
@scenario(FEATURE, "Clearing the search shows all requests again")
def test_search_cleared():
    pass


@given(parsers.parse('I am on the "{path}" page'))
def on_page(page: Page, path):
    page.goto(path)
    page.wait_for_load_state("networkidle")


@when(parsers.parse('I submit a feature request with title "{title}" and category "{category}"'))
def submit_request(page: Page, title, category):
    page.get_by_test_id("request-title").fill(title)
    page.get_by_test_id("request-category").select_option(category)
    with page.expect_response(lambda r: r.url.endswith("/api/feature-requests") and r.request.method == "POST"):
        page.get_by_test_id("request-submit").click()
    page.wait_for_load_state("networkidle")


@when(parsers.parse('I search the requests for "{text}"'))
def search(page: Page, text):
    page.get_by_test_id("request-search").fill(text)


@when("I clear the search")
def clear_search(page: Page):
    page.get_by_test_id("request-search").fill("")


@then(parsers.parse('the element "{testid}" contains the text "{text}"'))
def element_contains(page: Page, testid, text):
    expect(page.get_by_test_id(testid)).to_contain_text(text)


@then(parsers.parse('the element "{testid}" does not contain the text "{text}"'))
def element_not_contains(page: Page, testid, text):
    expect(page.get_by_test_id(testid)).not_to_contain_text(text)
