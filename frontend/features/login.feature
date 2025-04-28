Feature: Login
 
Scenario: Login successful
  Given I set franco as username 
  And 12345 as password
  When I click login
  Then I should see Difficulty Selection Page

Scenario: Login unsuccessful
  Given I set franco as username 
  And asdasdasd123123123 as password
  When I click login
  Then I should see a message Invalid username or password

