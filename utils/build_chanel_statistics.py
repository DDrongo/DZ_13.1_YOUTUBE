import json


"Возвращает статистику ютуб канала"
def build_chanel_statistics(youtube, channel_id ):
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    statistics = json.dumps(channel, indent=2, ensure_ascii=False)
    return statistics