from utils.build_chanel_statistics import build_chanel_statistics
from utils.get_api import get_api

class Channel():

    youtube_api = get_api()

    def __init__(self, channel_id=None):
        self.channel_id = channel_id

    def print_info(self):
        channel = build_chanel_statistics(self.youtube_api, self.channel_id)
        print(channel)


