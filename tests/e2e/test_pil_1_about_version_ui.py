"""Binds the page scenarios of PIL-1 (need a browser)."""

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenario, then

FEATURE = "PIL-1/about-version.feature"


@pytest.mark.e2e
@scenario(FEATURE, "About page displays the app version")
def test_about_shows_version():
    pass


@pytest.mark.e2e
@scenario(FEATURE, "Unknown page does not show a version")
def test_unknown_page_no_version():
    pass


@given(parsers.parse('I am on the "{path}" page'))
def on_page(page: Page, path):
    page.goto(path)


@then(parsers.parse('the element "{testid}" is visible'))
def element_visible(page: Page, testid):
    expect(page.get_by_test_id(testid)).to_be_visible()


@then(parsers.parse('the element "{testid}" contains the text "{text}"'))
def element_contains(page: Page, testid, text):
    expect(page.get_by_test_id(testid)).to_contain_text(text)


@then(parsers.parse('the element "{testid}" is not visible'))
def element_not_visible(page: Page, testid):
    expect(page.get_by_test_id(testid)).not_to_be_visible()
