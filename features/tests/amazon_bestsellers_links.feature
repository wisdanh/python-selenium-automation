# Created by trand at 2/24/2022
Feature: Test for amazon BestSellers page
  # Enter feature description here

  Scenario: Verify amount of links in amazon BestSellers page
    # Enter steps here
    Given Open amazon BestSellers page
    Then verify there are 5 links

