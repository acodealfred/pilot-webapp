Feature: Search feature requests

  Scenario: Search shows only matching requests
    Given I am on the "/feature-requests" page
    When I submit a feature request with title "Dark mode" and category "UI"
    And I submit a feature request with title "Faster search" and category "Performance"
    And I search the requests for "dark"
    Then the element "request-list" contains the text "Dark mode"
    And the element "request-list" does not contain the text "Faster search"

  Scenario: Search with no match shows a message
    Given I am on the "/feature-requests" page
    When I submit a feature request with title "Dark mode" and category "UI"
    And I search the requests for "zzz"
    Then the element "request-list" does not contain the text "Dark mode"
    And the element "request-empty" contains the text "No requests found"

  Scenario: Clearing the search shows all requests again
    Given I am on the "/feature-requests" page
    When I submit a feature request with title "Dark mode" and category "UI"
    And I submit a feature request with title "Faster search" and category "Performance"
    And I search the requests for "dark"
    And I clear the search
    Then the element "request-list" contains the text "Dark mode"
    And the element "request-list" contains the text "Faster search"

  Scenario: API filters requests by search text
    When I request "/api/feature-requests?q=zzz"
    Then the response status code is 200
    And the response is an empty list
