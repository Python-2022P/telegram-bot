import requests
from .user import User
from .update import Update
from .message import Message


class Bot:
    def __init__(self, token:str)->None:
        self.base_url = f'https://api.telegram.org/bot{token}'

    def getMe(self)->User:
        """A simple method for testing your bot's auth token.
         Returns:
          A telegram.User instance representing that bot if the
          credentials are valid, None otherwise.
        """
        url = self.base_url + '/getMe'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            user = User(data['result'])
            return user


        
    def getUpdates(self):
        """Use this method to receive incoming updates using long polling.
        Args:
            
        Returns:
          A  telegram.Update object is returned.
        """
        url=self.base_url+"/getUpdates"
        response=requests.get(url).json()["result"][-1]
        return Update(update=response)


    def sendMessage(self,chat_id,text):
        """Use this method to send text messages.
        Args:
          chat_id:
            Unique identifier for the message recipient — telegram.User or
            telegram.GroupChat id.
          text:
            Text of the message to be sent.
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendMessage"
        payload={"chat_id":chat_id,"text":text}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)

    
    def sendPhoto(self,
                  chat_id,
                  photo):
        """Use this method to send photos.
        Args:
          chat_id:
            Unique identifier for the message recipient — User or GroupChat id.
          photo:
            Photo to send. You can either pass a file_id as String to resend a
            photo that is already on the Telegram servers, or upload a new
            photo using multipart/form-data.
          caption:
            Photo caption (may also be used when resending photos by file_id).
            [Optional]
          reply_to_message_id:
            If the message is a reply, ID of the original message. [Optional]
          reply_markup:
            Additional interface options. A JSON-serialized object for a custom
            reply keyboard, instructions to hide keyboard or to force a reply
            from the user. [Optional]
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendPhoto"
        payload={"chat_id":chat_id,"photo":photo}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)
        

    def sendSticker(self,
                    chat_id,
                    sticker):
        """Use this method to send .webp stickers.
        Args:
          chat_id:
            Unique identifier for the message recipient — User or GroupChat id.
          sticker:
            Sticker to send. You can either pass a file_id as String to resend
            a sticker that is already on the Telegram servers, or upload a new
            sticker using multipart/form-data.
          reply_to_message_id:
            If the message is a reply, ID of the original message. [Optional]
          reply_markup:
            Additional interface options. A JSON-serialized object for a
            custom reply keyboard, instructions to hide keyboard or to force a
            reply from the user. [Optional]
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendMessage"
        payload={"chat_id":chat_id,"sticker":sticker}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)


    def sendLocation(self,
                     chat_id,
                     latitude,
                     longitude):
        """Use this method to send point on the map.
        Args:
          chat_id:
            Unique identifier for the message recipient — User or GroupChat id.
          latitude:
            Latitude of location.
          longitude:
            Longitude of location.
          reply_to_message_id:
            If the message is a reply, ID of the original message. [Optional]
          reply_markup:
            Additional interface options. A JSON-serialized object for a
            custom reply keyboard, instructions to hide keyboard or to force a
            reply from the user. [Optional]
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendLocation"
        payload={"chat_id":chat_id,"latitude":latitude,"longitude":longitude}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)


    def sendDocument(self,
                     chat_id,
                     document):
        """Use this method to send general files.
        Args:
          chat_id:
            Unique identifier for the message recipient — User or GroupChat id.
          document:
            File to send. You can either pass a file_id as String to resend a
            file that is already on the Telegram servers, or upload a new file
            using multipart/form-data.
          reply_to_message_id:
            If the message is a reply, ID of the original message. [Optional]
          reply_markup:
            Additional interface options. A JSON-serialized object for a
            custom reply keyboard, instructions to hide keyboard or to force a
            reply from the user. [Optional]
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendDocement"
        payload={"chat_id":chat_id,"document":document}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)

    
    def sendAudio(self,
                  chat_id,
                  audio):
        """Use this method to send audio files, if you want Telegram clients to
        display the file as a playable voice message. For this to work, your
        audio must be in an .ogg file encoded with OPUS (other formats may be
        sent as telegram.Document).
        Args:
          chat_id:
            Unique identifier for the message recipient — User or GroupChat id.
          audio:
            Audio file to send. You can either pass a file_id as String to
            resend an audio that is already on the Telegram servers, or upload
            a new audio file using multipart/form-data.
          reply_to_message_id:
            If the message is a reply, ID of the original message. [Optional]
          reply_markup:
            Additional interface options. A JSON-serialized object for a
            custom reply keyboard, instructions to hide keyboard or to force a
            reply from the user. [Optional]
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendAudio"
        payload={"chat_id":chat_id,"audio":audio}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)


    def sendVideo(self,
                  chat_id,
                  video):
        """Use this method to send video files, Telegram clients support mp4
        videos (other formats may be sent as telegram.Document).
        Args:
          chat_id:
            Unique identifier for the message recipient — User or GroupChat id.
          video:
            Video to send. You can either pass a file_id as String to resend a
            video that is already on the Telegram servers, or upload a new
            video file using multipart/form-data.
          reply_to_message_id:
            If the message is a reply, ID of the original message. [Optional]
          reply_markup:
            Additional interface options. A JSON-serialized object for a
            custom reply keyboard, instructions to hide keyboard or to force a
            reply from the user. [Optional]
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url=self.base_url+"/sendLocation"
        payload={"chat_id":chat_id,"video":video}
        response=requests.get(url,params=payload).json()["result"]
        
        return Message(response)
      
