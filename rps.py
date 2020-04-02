from enum import Enum
from random import randint
from PyInquirer import style_from_dict, Token, prompt, Separator

choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
outcomes = {0: "Draw", 1: "Win", 2: "Loss"}

outcome_by_choice = {
  0: {
    0: 0,
    1: 2,
    2: 1
    },
  1: {
    0: 1,
    1: 0,
    2: 2
    },
  2: {
    0: 2,
    1: 1,
    2: 0
    } 
  }

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

choice = [
  {
    "type": "list",
    "message": "Select your choice",
    "name": "choice",
    "choices": [
      {"name": "Rock", "value": 0},
      {"name": "Paper", "value": 1},
      {"name": "Scissors", "value": 2}
    ],
    'validate': lambda answer: 'You must choose at least one topping.' \
      if len(answer) == 0 else True
  }
]

choice = prompt(choice, style=style)
oponentsChoice = randint(0, 2)
outcome = outcome_by_choice[choice["choice"]][oponentsChoice]

print(f"Your oponent's choice: {choices[oponentsChoice]}")
print(f"Outcome: {outcomes[outcome]}")