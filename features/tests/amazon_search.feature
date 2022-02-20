# Created by trand at 2/19/2022
Feature: Cancelling an order on Amazon help page
  # Enter feature description here

  Scenario: Users can search for Cancelling an order on Amazon help page
    # Enter steps here
    Given Open Amazon help page
    When Input Cancel order into Search Help Library field
    Then Cancel items or Orders are present