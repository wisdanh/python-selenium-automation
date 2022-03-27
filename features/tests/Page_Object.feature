# Created by trand at 3/26/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
  Given Open Amazon main page
  When Click Amazon Orders link
  Then Verify Sign In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
  Given Open Amazon page
  When Click on Cart figure icon
  Then Verify 'Your Shopping Cart is empty' text present
