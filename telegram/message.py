import json
from .user import User
from .chat import Chat
from .photosize import PhotoSize


class Message:
    def __init__(self, message: dict) -> None:
        self.message_id  = message['message_id']
        self.from_user   = User(message['from'])
        self.chat        = Chat(message['chat'])
        self.text        = message.get('text')
        self.photo       = []
    
        for files in message.get('photo', ''):
            self.photo.append(PhotoSize(files))


    def to_dict(self)->dict:
        '''Returns a dictionary representation of the object.'''
        return {
            'message_id': self.message_id,
            'from': self.from_user.to_dict(),
            'chat': self.chat.to_dict(),
            'text': self.text,
            'photo': [photo.to_dict() for photo in self.photo]
        }
    
    def reply_text(self, text: str) -> None:
        '''Sends a text message to the chat.'''
        return json.dumps(self.to_dict(), indent=4)


    def reply_photo(self, photo: str) -> None:
        '''Sends a photo to the chat.'''
        pass


    def reply_video(self, video: str) -> None:
        '''Sends a video to the chat.'''
        pass


    def __str__(self) -> str:
        '''Returns a string representation of the object.'''
        return json.dumps(self.to_dict(), indent=4)
    