from .db import db
from .abstract_model import AbstractModel


class MessageModel(AbstractModel):
    _collection = db["chat"]

    def to_dict(self):
        return {
            "content": self.data["content"],
            "to": self.data["to"],
            "from": self.data["from"],
            "time": self.data["time"],
        }
