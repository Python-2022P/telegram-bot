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
        return {
            'file_id': self.file_id,
            'file_unique_id': self.file_unique_id,
            'width': self.width,
            'height': self.height,
            'file_size': self.file_size
        }

    
    def __str__(self) -> str:
        '''Returns a string representation of the object.'''
        return json.dumps(self.to_dict(), indent=4)