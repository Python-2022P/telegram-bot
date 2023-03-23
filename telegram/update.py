import json
from .message import Message

class Update:
    def __init__(self, update) -> None:
        self.update_id = update['update_id']
        self.message   = Message(update['message'])

    
    def to_dict(self)->dict:
        '''Returns a dictionary representation of the object.'''
        return {
            'update_id': self.update_id,
            'message': self.message.to_dict()
        }


    def __str__(self) -> str:
        '''Returns a string representation of the object.'''
        return json.dumps(self.to_dict(), indent=4)
    