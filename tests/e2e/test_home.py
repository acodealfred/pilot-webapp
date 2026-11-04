import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_home_shows_title_and_health(page: Page):
    page.goto("/")

    expect(page.get_by_test_id("page-title")).to_have_text("Spear818 Pilot")
    expect(page.get_by_test_id("health-status")).to_have_text("ok")
