Feature: Login
 
Scenario: Login successful
  Given I set franco as username 
  And 12345 as password
  When I click login
  Then I should see Difficulty Selection Page

