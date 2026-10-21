# Coding Assignment 4

> Note: Ensure you have installed **Pygame** and have a basic understanding of Python control structures and functions (Steps 1–8 of the Learning Path) before attempting this assignment.

Most people think games are fun! And a lot of those people have wondered to themselves the following questions:

- How do I make a game?
- Can *I* make a game?
- Would I like making a game?

I know early on in my education, I had wondered all of these things. I also know that I was intimidated by the idea of making a game. I thought it would be too hard, and I didn't know where to start. 

This assignment is designed to introduce you to creating a simple game using a libarary called `Pygame`. You will set up a game window, handle user input, and implement basic game mechanics.

!!! Tip "Pygame Installation"
    To install Pygame, run the following command in your terminal or command prompt:
    
    ```bash
    pip install pygame
    ```

## What you'll do in this coding assignment

You aren't really required to do much work in this assignment, below you will find three "problems" that all already have solutions. The blanks are already filled in, all you need to do is go through and remove the comments from the code. 

So, what this coding assignment is really doing is (1) testing your ability to install a new library (`pygame`) on your computer and (2) provide you the opportunity to see how a game is structured. 

!!! Tip "If you're taking this for credit" 
    Because you're not writing code here, you will not be needing to submit a `.py` file, instead take three screenshots of the three different resulting programs below, and submitting those screenshots. If you don't know how to take a screenshot, Google it or ask a chatbot :)

    *Alternatively*, you can create your own little game! Any game you want or can think of, you can even use a chatbot to help you. If you go this route, you'll submit a `.py` file of your game following this format: `lastname_firstname_coding_assignment_4.py`.

## Problem 1: Setting Up the Game Window

Write a Python program using Pygame that:

- Imports Pygame and initializes it.
- Creates a window of size **640×480** pixels.
- Sets the window title to **"My First Pygame Window"**.
- Fills the window with a background color of your choice.
- Includes a game loop that keeps the window open until the user closes it.

> Tip: Remember to call `pygame.quit()` after your game loop ends.

```python
# coding_assignment_05.md – Problem 1 starter

import pygame

def main():
    # TODO: Initialize Pygame
    # pygame.init()
    
    # TODO: Set up the game window
    # screen = pygame.display.set_mode((640, 480))
    
    # TODO: Set window title
    # pygame.display.set_caption("My First Pygame Window")
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # TODO: Fill the screen with a color
        # screen.fill((30, 30, 30))
        
        pygame.display.flip()
    
    # TODO: Quit Pygame
    # pygame.quit()

if __name__ == "__main__":
    main()
```
### What's going on here?
- `pygame.init()` initializes all the Pygame modules.
- `pygame.display.set_mode()` creates a window with the specified dimensions.
- `pygame.display.set_caption()` sets the title of the window.
- The game loop handles events (like closing the window) and updates the display.
- `pygame.display.flip()` updates the entire screen with the new content.
- `pygame.quit()` cleans up and closes the Pygame window.

## Problem 2: Player Movement

Extend your program from **Problem 1** to:

1. Draw a **player rectangle** (50×50 px) at the center of the screen.
2. Move the rectangle using the **arrow keys** (Up, Down, Left, Right) at a constant speed.
3. Prevent the rectangle from moving off-screen.

> Hint: Use `pygame.key.get_pressed()` to check multiple keys at once.

```python
# coding_assignment_05.md – Problem 2 starter

import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move the Square")
    clock = pygame.time.Clock()
    
    # Player setup
    player_size  = 50
    player_x     = (640 - player_size) // 2
    player_y     = (480 - player_size) // 2
    player_speed = 5
    
    running = True
    while running:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        # TODO: Update player_x and player_y based on keys
        # if keys[pygame.K_LEFT]:  player_x -= player_speed
        # if keys[pygame.K_RIGHT]: player_x += player_speed
        # if keys[pygame.K_UP]:    player_y -= player_speed
        # if keys[pygame.K_DOWN]:  player_y += player_speed
        
        # TODO: Keep player within screen bounds
        # player_x = max(0, min(player_x, 640 - player_size))
        # player_y = max(0, min(player_y, 480 - player_size))
        
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0),
                         (player_x, player_y, player_size, player_size))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
```

### What's going on here?
- `pygame.time.Clock()` is used to control the frame rate, meaning how many times the screen updates per second.
- `pygame.draw.rect()` (towards the end of the code) draws the player rectangle on the screen.
- The player rectangle is initialized at the center of the screen (that's what the 640 and 480 are for, the size of the window, which then you divide by 2. Think of the screen like a coordinate grid).
- `pygame.key.get_pressed()` checks the state of all keys.
- The player rectangle's position is updated based on the pressed keys.
- When you press the arrow keys, the rectangle moves in the corresponding direction.
- The `max()` and `min()` functions ensure the rectangle stays within the window bounds.
- The screen is cleared and redrawn every frame to reflect the updated position of the player rectangle.

??? Tip "Thinking about the game loop"
    An important concept in game development is the **game loop** and corresponding **frame rate**. The game loop is a continuous loop that runs until the game is closed. It handles events, updates the game state, and renders the graphics.

    A lot of the work of programming a game is thinking about how to structure your code within the game loop -- doing things like checking to see if a player is near an object, and if they are, updating the game state to reflect that so they can interact with said object.

## Problem 3: Bouncing Ball

Further extend your program to include:

1. A **ball** (circle) that starts at a random position and moves at a constant velocity.
2. The ball should **bounce** off all four edges of the window.
3. Draw the ball and update its position every frame.

> Tip: Use `pygame.draw.circle()` to draw the ball, and reverse the velocity component when it hits an edge.

```python
# coding_assignment_05.md – Problem 3 starter

import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Bouncing Ball")
    clock = pygame.time.Clock()
    
    # Ball setup
    ball_radius = 15
    ball_x      = random.randint(ball_radius, 640 - ball_radius)
    ball_y      = random.randint(ball_radius, 480 - ball_radius)
    vel_x       = 3
    vel_y       = 3
    
    running = True
    while running:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # TODO: Update ball_x and ball_y
        # ball_x += vel_x
        # ball_y += vel_y
        
        # TODO: Bounce off edges
        # if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 640:
        #     vel_x = -vel_x
        # if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 480:
        #     vel_y = -vel_y
        
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0, 255, 0),
                           (ball_x, ball_y), ball_radius)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
```
### What's going on here?
- The ball is initialized at a random position within the window, ensuring it doesn't start off-screen.
- The ball's velocity is set to a constant value, which determines how fast it moves.
- The ball's position is updated every frame based on its velocity.
- The ball bounces off the edges of the window by reversing its velocity when it hits an edge.
- `pygame.draw.circle()` draws the ball on the screen.
- The screen is cleared and redrawn every frame to reflect the updated position of the ball.

??? Question "Does this feel less like a game?"
    It might! Notice how we removed player movement and the game loop is now just a ball bouncing around. 
    
    You could imagine how a more fun game would include a player trying to dodge or catch the ball -- to do that you'd need to program new behaviors that include things like:
    
    - checking for collisions between the player and the ball
    - updating the game state to reflect that the player has caught/been hit by the ball
    - updating the score based on the player catching/hitting the ball

___

Congratulations! You’ve created a basic Pygame program with window setup, player movement, and a bouncing ball.  

Feel free to experiment by adding:
- **Collision detection** between the player and the ball.
- A **score counter** that increments on each bounce.
- Different **colors** or **sprites** instead of simple shapes.

When you are satisfied, ensure all your solutions are tested and functioning as expected. Submit your work as a Python script (`.py`) or a Jupyter Notebook (`.ipynb`) on Canvas.
