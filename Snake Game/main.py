from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from wall import Wall
import tkinter as tk

def start_game(level, root_start):
    root_start.destroy() 
    screen = Screen() 
    screen.setup(680, 710)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)    
    wall = Wall()
    if level == "Easy":
        wall.easy_level()
    elif level == "Medium":
        wall.medium_level()
    else:
        wall.hard_level()
    scoreboard = ScoreBoard()
    scoreboard.load_high_score(level)
    snake = Snake(level)
    food = Food(level)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.position_snake([segment.pos() for segment in snake.segments])
            food.refresh()
            snake.extend()
            scoreboard.score_increase()

        # Detect collision with wall.
        for i in wall.walls[:]:
            if snake.head.distance(i) < 19:
                scoreboard.save_high_score(level)
                game_is_on = False
                screen.clear()
                restart_screen(scoreboard.high_score, scoreboard.score)

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.save_high_score(level)
                game_is_on = False
                screen.clear()
                restart_screen(scoreboard.high_score, scoreboard.score)

    screen.exitonclick()

def create_buttons_start(root_start):
    easy_button = tk.Button(root_start, text="Easy", command=lambda: start_game("Easy", root_start), padx=20, pady=10, font=("Helvetica", 16))
    medium_button = tk.Button(root_start, text="Medium", command=lambda: start_game("Medium", root_start), padx=20, pady=10, font=("Helvetica", 16))
    hard_button = tk.Button(root_start, text="Hard", command=lambda: start_game("Hard", root_start), padx=20, pady=10, font=("Helvetica", 16))
    
    easy_button.pack(fill=tk.BOTH, expand=True)
    medium_button.pack(fill=tk.BOTH, expand=True)
    hard_button.pack(fill=tk.BOTH, expand=True)

def create_buttons_restart(root_restart):
    restart_button = tk.Button(root_restart, text="Restart", command=lambda: start_screen(root_restart), padx=20, pady=10, font=("Helvetica", 16))
    exit_button = tk.Button(root_restart, text="   Exit   ", command=lambda: end_game(), padx=20, pady=10, font=("Helvetica", 16))
    restart_button.pack()
    exit_button.pack()

def start_screen(root_restart=None):
    if root_restart is not None:
        root_restart.destroy()
    root_start = tk.Tk()
    root_start.title("Select Game Level")
    root_start.geometry(f"{300}x{400}+{(root_start.winfo_screenwidth() - 300) // 2}+{(root_start.winfo_screenheight() - 400) // 2}")
    create_buttons_start(root_start)
    root_start.mainloop()

def restart_screen(best_score, current_score):    
    root_restart = tk.Tk()
    root_restart.title("")
    label_game_over = tk.Label(root_restart, text="GAME OVER", font=("Helvetica", 16))
    label_current_score = tk.Label(root_restart, text=f"Current Score: {current_score}", font=("Helvetica", 16))
    label_best_score = tk.Label(root_restart, text=f"Best Score: {best_score}", font=("Helvetica", 16))
    label_game_over.pack()
    label_current_score.pack()
    label_best_score.pack()
    root_restart.geometry(f"{300}x{400}+{(root_restart.winfo_screenwidth() - 300) // 2}+{(root_restart.winfo_screenheight() - 400) // 2}")
    create_buttons_restart(root_restart)
    root_restart.mainloop()

def end_game():
    exit()

start_screen()