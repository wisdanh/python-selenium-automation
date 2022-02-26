# Created by trand at 2/25/2022
Feature: Amazon cart items

  Scenario: Verify number of items in cart
    Given Open Amazon
    When Search for shot glass
    And Click on first product
    And Click on Add to Cart button
    And Open cart page
    Then Verify cart has 1 item(s)