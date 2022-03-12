# Snake-Game
The famous Snake Game built using Python Turtle.
It is simple to play - Use arrow keys to move. You cannot turn in opposite direction just by pressing the opposite key.
To freeze the program, press 'f'. You cannot unfreeze(continue) the program, that functionality is not added yet.

# Run the Program
To Run the Program: Open it in PyCharm(prefered IDE). You can use some other IDE too if you want, and click on Run button.

# How it works?
Snake here is a list of turtles.
A while loop keeps calling the move method on snake object which move the head of snake by one unit(I have taken that as 20).
Inside the snake class, due to move method, we move last item to second last position, second last position to third last and so on till head.
Everytime it comes in contact with food, a new turtle is appended to snake body.
Press space bar to pause or resume the game.
We record the all-time highscore in a text file.

# Improvement Needed
Anyone reading this, I require your help to make my snake look more snake like, i.e., to add an image of snake head for head and some scale images for the body.

# Improvements Made
<ol>
  <li>
    High score updates as soon as the score surpasses it. Earlier it updated only when the game restarted due to snake biting its own body or hitting the wall or game restart.  
  </li>
  <li>
    Added the feature to pause or resume the game with one keypress. Here just press the space bar to do so.  
  </li>
  <li>
    Now that snake head and body can be differentiated from one another due to difference in their colors, earlier both of them were white squares.  
  </li>
</ol>
