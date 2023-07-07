Description:
The Pong game you shared is a simple implementation of the classic Pong game using Python and the Turtle graphics library.

Libraries Used:
Turtle: The Turtle library is a built-in Python library that provides a simple way to create graphics and animations. It is used in this game to create the game window, paddles, ball, and handle the game's animation and movement.
OS: The OS library is used to manage the sounds in the game.

Techniques Employed:
Game Loop: The main game loop is a while loop that continuously updates the game state and handles user input. It ensures that the game runs smoothly by updating the positions of the paddles and ball, detecting collisions, and updating the scores.
Keyboard Input: The game captures keyboard input using the wn.onkeypress() function from the Turtle library.
Collision Detection: The game checks for collisions between the ball and the paddles, as well as the ball and the top/bottom boundaries of the game window. This allows the ball to bounce off the paddles and walls.
Score Tracking: The game keeps track of the score for each player (Player A and Player B) using the score_a and score_b variables. The scores are displayed on the screen using the Turtle library's pen object.
Sound Effects: The game incorporates sound effects using the os.system() function to play audio files when certain events occur, such as the ball hitting the paddles, scoring points, or the game ending.

![pong_thumbnail_photo](https://github.com/PeterStoyanov83/PONG/assets/108938447/ac346051-d0c1-473a-9cf0-4d37e4cee901)

