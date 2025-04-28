Feature: Ingame words Input
 
Scenario: Guess a correct word
  Given I click login as anonimous
  When I select a difficulty
  And I click play
  Then The game starts
  When I click risk a word
  And I guess test as word
  Then I see Ganaste!

Scenario: Guess a wrong word
  Given I click login as anonimous
  When I select a difficulty
  And I click play
  Then The game starts
  When I click risk a word
  And I guess prueba as word
  Then I see prueba in wrong risked words list