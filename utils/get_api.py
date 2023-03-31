import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

"формерует ключ доступа к ютуб"

def get_api():

    load_dotenv()
    api_key = os.environ.get('DDrongoSkyproYoutubeAPIkey')
    youtube = build("youtube", "v3", developerKey=api_key)

    return youtube

