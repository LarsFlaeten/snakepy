# snakepy
A simple snake game I wrote with my kids. The idea was to demonstrate simple programming and how to develop the game based on rules we discussed and implemented.

This is a gret way to demonstate to kids how games (or computer programs in general) are developed in a simple way.

To run:
```python3 snake.py```

# Development
- We startet with a red blob you could move around with the arrow buttons.
- Added a "grid" to mimic the older snake games movement style
- Made the snake move by itself, and the arrow buttons only changed direction.  Add the concept of speed.
- Added the concept of snake length, added an array that kept track of positions
- Added apples that would increase the lenght of the snake if the head coincided with the fruit position. Test how different speeds made it harder to hit the food.
- Major design change: Fruit should be replaced with a pancake (Requirement from the kids)
- Place a new pancake at a random position once the previous had been eaten
- Implement collission detection against walls (certain death!)
- Implement a points counter
