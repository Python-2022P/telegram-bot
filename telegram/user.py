import json


class User:
    def __init__(self,user):
        self.id = user.get('id')
        self.first_name=user.get('first_name')
        self.last_name=user.get('last_name')
        self.username = user.get('username')
        self.is_bot = user.get('is_bot')
        self.language_code = user.get('language_code')
        self.is_premium = user.get('is_premium')
        self.added_to_attachment_menu = user.get('added_to_attachment_menu')
        self.can_join_groups = user.get('can_join_groups')
        self.can_read_all_group_messages = user.get('can_read_all_group_messages')
        self.supports_inline_queries = user.get('supports_inline_queries')


    def to_dict(self)->dict:
        '''Returns a dictionary representation of the object.'''
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'is_bot': self.is_bot,
            'language_code': self.language_code,
            'is_premium': self.is_premium,
            'added_to_attachment_menu': self.added_to_attachment_menu,
            'can_join_groups': self.can_join_groups,
            'can_read_all_group_messages': self.can_read_all_group_messages,
            'supports_inline_queries': self.supports_inline_queries
        }


    def __str__(self) -> str:
        '''Returns a string representation of the object.'''
        return json.dumps(self.to_dict(), indent=4)