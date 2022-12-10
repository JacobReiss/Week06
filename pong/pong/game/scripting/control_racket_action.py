#from tkinter import LEFT, RIGHT
from constants import *
from game.scripting.action import Action

class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, collection, script, callback):
        racket_a = collection.get_entity_by_idx(RACKET_GROUP, PLAYER_1_IDX)
        racket_b = collection.get_entity_by_idx(RACKET_GROUP, PLAYER_2_IDX)
        
        if self._keyboard_service.is_key_down(PLAYER_1_KEY_UP):
            racket_a.swing_up()
        elif self._keyboard_service.is_key_down(PLAYER_1_KEY_DOWN):
            racket_a.swing_down()
        else:
            racket_a.stop_moving()
        
        if self._keyboard_service.is_key_down(PLAYER_2_KEY_UP):
            racket_b.swing_up()
        elif self._keyboard_service.is_key_down(PLAYER_2_KEY_DOWN):
            racket_b.swing_down()
        else:
            racket_b.stop_moving()
    