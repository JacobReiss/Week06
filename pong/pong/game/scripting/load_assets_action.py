from game.scripting.action import Action
#from constants import GAME_ROOT_FOLDER
import os

class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, collection, script, callback):
        self._audio_service.load_sounds('pong/assets/sounds')
        self._video_service.load_fonts('pong/assets/fonts')
        self._video_service.load_images('pong/assets/images')