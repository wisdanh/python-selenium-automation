# Created by trand at 2/19/2022
Feature:
#  Scenario: Users can search for Cancelling an order on Amazon help page
#    # Enter steps here
#    Given Open Amazon help page
#    When Input Cancel order into Search Help Library field
#    Then Cancel items or Orders are present

  Modified on 4/2/2022
  Scenario: Users can see the deals on New Arrivals when hover over
    Given Open Amazon B074TBCSC8 product page
    When Hover over New Arrivals
    Then  Girl deals show up

  Scenario: User can select and search in a department
      Given Open Amazon main page
      When Select appliances department
      And Search for refrigerator
      Then Verify appliances department is selected