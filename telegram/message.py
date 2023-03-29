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
            "messge_id":self.message_id,
            "from_user":self.from_user,
            "chat":self.chat,
            "text":self.text,
            "photo":self.photo
        }

    
    def reply_text(self, text: str) -> None:
        '''Sends a text message to the chat.'''
        
        
        


    def reply_photo(self, photo: str) -> None:
        '''Sends a photo to the chat.'''
        pass


    def reply_video(self, video: str) -> None:
        '''Sends a video to the chat.'''
        pass


    def __str__(self) -> str:
        '''Returns a string representation of the object.'''
        return json.dumps(self.to_dict(),indent=4)
    