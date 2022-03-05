import importlib
from turtle import color
import constants
import pyray
from constants import MAX_X, MAX_Y

from game.casting.cast import Cast
from game.casting.food import Food
# from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food()) - might add at later time.
    x = MAX_X / 4
    y = MAX_Y / 4
    cast.add_actor("snake_1", Snake(x, y, constants.GREEN))
    x = x * 3
    cast.add_actor("snake_2", Snake(x, y, constants.RED))
    # cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input_1", ControlActorsAction(keyboard_service, "snake_1", "a", "d", "w", "s"))
    script.add_action("input_2", ControlActorsAction(keyboard_service, "snake_2", "j", "l", "i", "k"))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()