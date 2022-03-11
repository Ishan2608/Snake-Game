# Snake-Game
The famous Snake Game built using Python Turtle.
It is simple to play - Use arrow keys to move. You cannot turn in opposite direction just by pressing the opposite key.
To freeze the program, press 'f'. You cannot unfreeze(continue) the program, that functionality is not added yet.

# Run the Program
To Run the Program: Open it in PyCharm(prefered IDE). You can use some other IDE too if you want, and click on Run button.

# Improvement Needed
Anyone reading this, I require your help to add the unfreeze functionality in my program, I have tried various ways but none of them work. 
It would be great if you could help me out.

# How it works?
Snake here is a list of turtles.
A while loop keeps calling the move method on snake object which move the head of snake by one unit(I have taken that as 20).
Inside the snake class, due to move method, we move last item to second last position, second last position to third last and so on till head.
Everytime it comes in contact with food, a new turtle is appended to snake body.
We record the all-time highscore in a text file.
