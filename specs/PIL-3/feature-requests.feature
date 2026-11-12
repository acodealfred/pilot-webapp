Feature: Submit and view feature requests

  Scenario: Submitted request appears in the list
    Given I am on the "/feature-requests" page
    When I submit a feature request with title "Dark mode", description "Add a dark theme" and category "UI"
    Then the element "request-list" contains the text "Dark mode"
    And the element "request-list" contains the text "UI"

  Scenario: Newest request is listed first
    Given I am on the "/feature-requests" page
    When I submit a feature request with title "First idea" and category "Other"
    And I submit a feature request with title "Second idea" and category "Performance"
    Then the first item in "request-list" contains the text "Second idea"

  Scenario: Request without a title is rejected
    Given I am on the "/feature-requests" page
    When I submit a feature request with an empty title and category "UI"
    Then the element "request-error" is visible
    And the element "request-error" contains the text "Title is required"
    And no request is added to "request-list"

  Scenario: Request with an unknown category is rejected by the API
    When I post a feature request with title "Faster search" and category "Security"
    Then the response status code is 422
