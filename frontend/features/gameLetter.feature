Feature: Ingame letters Input 

Scenario: Guess a correct letter
  Given I click login as anonimous
  When I select a difficulty
  And I click play
  Then The game starts
  When I guess E as letter
  Then I see E in the word to guess