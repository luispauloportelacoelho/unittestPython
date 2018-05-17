Feature: Sum numbers

  Scenario: basic sum
    When Sum "2" with "2"
    Then the result is "4"

  Scenario: sum of float values
    When Sum "2.0" with "2.0"
    Then the result is "4.0"
