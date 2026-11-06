Feature: Service health
  As an operator
  I want a health endpoint
  So that CI and monitoring can check that the service is running

  Scenario: Health endpoint reports ok
    When I request "/api/health"
    Then the response status code is 200
    And the response field "status" is "ok"
