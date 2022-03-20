# Created by trand at 3/19/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
   Given Open Amazon T&C page
   And Store original windows
   When Click on Amazon Privacy Notice link
   And Switch to the newly opened window
   Then Verify Amazon Privacy Notice page is opened
   And User can close new window
   And User switch back to original
