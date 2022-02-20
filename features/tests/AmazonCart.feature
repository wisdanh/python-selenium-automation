# Created by trand at 2/20/2022
Feature: Your Amazon Cart is empty
  # Enter feature description here

  Scenario: Verify that Your Amazon Cart is empty
    # Enter steps here
    Given Open Amazon page
    When Click on Cart icon
    Then Your Amazon Cart is empty
