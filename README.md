# alien_invasion

A game that is essentially a clone of the classic, “Space Invaders.”

Was used as an opportunity to continue learning Python as well as the Pygame library

To build and run, clone the repository, and then from the alien_invasion project directory type:

pip3 install -r requirements.txt

This line will install any dependencies required to be able to run the program. Afterwards, type to run the game:

python3 alien_invasion.py

Specifications:

There are five rows of aliens that are moving left and right withing the borders of the window. As the aliens move side to side, they slows move downwards towards the player as well.

The player is able to move horizontally using the left and right arrow keys, but is unable to move vertically. The player can also shoot bullets at the aliens by pressing spacebar.

TODO:

Currently the game ends when all the aliens are defeated, but I would like to have the aliens respawn and maybe move faster.

I would like to implement a points system to keep track of how many aliens were shot as well as grant more points the more they kill.

There is currently no implementation of what happens when an alien touches the player’s ship or moves past the player.

I would also like to implement a life system so the player has three chances.

![screenshot_20210728_142706](https://user-images.githubusercontent.com/48459796/127277621-d0e7662e-6fa0-4a32-ba6e-7053a21e8f6b.png)
