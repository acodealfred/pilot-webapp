"""Binds the page scenarios of PIL-3 (need a browser)."""

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenario, then, when

FEATURE = "PIL-3/feature-requests.feature"


@pytest.fixture
def state():
    return {}


@pytest.mark.e2e
@scenario(FEATURE, "Submitted request appears in the list")
def test_submitted_request_listed():
    pass


@pytest.mark.e2e
@scenario(FEATURE, "Newest request is listed first")
def test_newest_first():
    pass


@pytest.mark.e2e
@scenario(FEATURE, "Request without a title is rejected")
def test_missing_title_rejected():
    pass


@given(parsers.parse('I am on the "{path}" page'))
def on_page(page: Page, state, path):
    page.goto(path)
    page.wait_for_load_state("networkidle")
    # The server keeps requests in memory across tests, so count what is already listed.
    state["initial_count"] = page.get_by_test_id("request-item").count()


def _submit(page: Page, title, category, description=""):
    page.get_by_test_id("request-title").fill(title)
    page.get_by_test_id("request-description").fill(description)
    page.get_by_test_id("request-category").select_option(category)
    with page.expect_response(lambda r: r.url.endswith("/api/feature-requests") and r.request.method == "POST"):
        page.get_by_test_id("request-submit").click()
    page.wait_for_load_state("networkidle")


@when(
    parsers.parse(
        'I submit a feature request with title "{title}", description "{description}" and category "{category}"'
    )
)
def submit_full(page: Page, title, description, category):
    _submit(page, title, category, description)


@when(parsers.parse('I submit a feature request with title "{title}" and category "{category}"'))
def submit_request(page: Page, title, category):
    _submit(page, title, category)


@when(parsers.parse('I submit a feature request with an empty title and category "{category}"'))
def submit_empty_title(page: Page, category):
    _submit(page, "", category)


@then(parsers.parse('the element "{testid}" is visible'))
def element_visible(page: Page, testid):
    expect(page.get_by_test_id(testid)).to_be_visible()


@then(parsers.parse('the element "{testid}" contains the text "{text}"'))
def element_contains(page: Page, testid, text):
    expect(page.get_by_test_id(testid)).to_contain_text(text)


@then(parsers.parse('the first item in "{testid}" contains the text "{text}"'))
def first_item_contains(page: Page, testid, text):
    expect(page.get_by_test_id(testid).get_by_test_id("request-item").first).to_contain_text(text)


@then(parsers.parse('no request is added to "{testid}"'))
def no_request_added(page: Page, state, testid):
    expect(page.get_by_test_id("request-item")).to_have_count(state["initial_count"])
