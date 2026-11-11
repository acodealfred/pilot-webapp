Feature: About page shows the app version

  Scenario: Version endpoint reports the app version
    When I request "/api/version"
    Then the response status code is 200
    And the response field "version" is "0.1.0"

  Scenario: About page displays the app version
    Given I am on the "/about" page
    Then the element "app-version" is visible
    And the element "app-version" contains the text "0.1.0"

  Scenario: Unknown page does not show a version
    Given I am on the "/not-a-page" page
    Then the element "app-version" is not visible
