from datetime import datetime


class Meldung:
    def __init__(self, user_id, image, longitude, latitude, timestamp, category=None, recyclable=None ):
        self.user_id = user_id
        self.image = image
        self.longitude = longitude
        self.latitude = latitude
        self.time_stamp = timestamp
        self.category = category
        self.recyclable = recyclable

    def to_json(self):
        return {
            "user_id": self.user_id,
            "image": self.image,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "time_stamp": self.time_stamp,
            "category": self.category,
            "recycling": self.recyclable
        }
