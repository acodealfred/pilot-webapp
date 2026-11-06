"""Reusable BDD steps for API scenarios.

Story test modules only need to bind their feature file with `scenarios(...)`
and add any steps that are specific to the story.
"""

import pytest
from pytest_bdd import parsers, then, when


@pytest.fixture
def context():
    return {}


@when(parsers.parse('I request "{path}"'))
def request_path(client, context, path):
    context["response"] = client.get(path)


@then(parsers.parse("the response status code is {code:d}"))
def response_status(context, code):
    assert context["response"].status_code == code


@then(parsers.parse('the response field "{field}" is "{value}"'))
def response_field(context, field, value):
    assert str(context["response"].json()[field]) == value
