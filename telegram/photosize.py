import json

class PhotoSize:
    def __init__(self, photo: dict) -> None:
        self.file_id = photo['file_id']
        self.file_unique_id = photo['file_unique_id']
        self.width = photo.get('width')
        self.height = photo.get('height')
        self.file_size = photo.get('file_size')


    def to_dict(self)->dict:
        '''Returns a dictionary representation of the object.'''
        pass

    
    def __str__(self) -> str:
        '''Returns a string representation of the object.'''
        pass