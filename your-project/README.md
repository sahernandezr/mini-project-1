<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Let's Play Tic Tac Toe
*Sandra Hernández*

*Data Analysis Full Time, Mexico City, October 2022

<img src="https://media1.tenor.com/images/aef72d3acb463a23ad8b8c951d87ff53/tenor.gif" width="150"/>


## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This is a command line game of tic tac toe, built with Python using classes.
Using numpy, a 'toin coss' decides who goes first, the user or the computer, and itertools and Python's collections are used to check if there is a winner after each move.

## Rules
- The board is a grid of 3x3.
- Two players: X and O. X always plays first.
- On their turn, each player places their mark in a square of the grid.
- The winner is the first player that places 3 of their marks in a row (vertical, horizonal or diagonal). 
- If the grid is full of tokens and no lines are formed, a tie is declared.

## Workflow
1. Pseudocode: writing how a round plays out, I was able to identify several actions that had to happen several times, so those were coded as functions.
2. Flowchart: Each step of the process is related to a different entity (the board, a player, a specific round), that were the basis of the classes used and helped identify which function belonged to which class.
3. The basic elements to play a game were identified to define an MVP. Extras were listed as possible improvements for the future. 
4. There are just eight possible winning results on Tic Tac Toe. To determine the winner, the spaces occupied by each player are used to calculate all possible 3 element combinations and then those are compared with the possible winning results to check for a match. 
    
## Organization
With Trello, each step was a card and inside each card, the possible steps where listed. 
Deadlines were added to each card.

The repository as a file for classes and another one to start the game. If the grid is improved with graphics in the future, those will have their own folder.

## Links
[Repository](https://github.com/sahernandezr/mini-project-1/tree/master/your-project)  
[Slides](https://www.canva.com/design/DAFQKZRwH4g/n7RfiOef06Nqw6bxDxbeuw/view?utm_content=DAFQKZRwH4g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)  
[Trello](https://trello.com/b/FprQ67UI/daft-mini-project-1-game)  