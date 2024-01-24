Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open orange HRM homepage
    And Enter username "admin" and password "admin123"
    And click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to Orange HRM with multiple parameters
    Given I launch chrome browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
