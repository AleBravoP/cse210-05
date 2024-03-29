from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        snake_1 = cast.get_first_actor("snake_1")
        snake_2 = cast.get_first_actor("snake_2")
        segments_1 = snake_1.get_segments()
        segments_2 = snake_2.get_segments()
        messages = cast.get_actors("messages")

         # This will make the tail grow by one for each cell it advances 
        # (leave it fixated to the starting point)
        snake_1.grow_tail(1)
        snake_2.grow_tail(1)

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments_1)
        self._video_service.draw_actors(segments_2)
        # self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()