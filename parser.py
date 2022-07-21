from collections import Counter
from googlesheet import USERS_DICT


class UsersData:
    users_dict = USERS_DICT
    """ 
    Processes the dictionary received by google api 
    based on the requests that the user sends to 
    the bot in a telegram
    """
    @staticmethod
    def get_suitable_users(answer, users_dict):
        """
        Based on the response from the user in the telegram, delet from dict 
        those contacts that do not contain the selected type
        """
        result = users_dict.copy()
        for item in users_dict.keys():
            if answer not in item:
                result.pop(item)
        return result

    @classmethod
    def create_types_ranking(cls):
        """
        create tuple with most common types and sort it
        from the most common type to the least
        """
        types_list = list(cls.users_dict.keys())
        types_ranking = Counter((",".join(types_list)).split(','))
        del types_ranking[' ']
        return types_ranking.most_common()

    @classmethod
    def get_types_from_dict(cls, user_dict):
        user_type = []
        [user_type.append(_type) for _type in user_dict.keys()]
        return '|'.join(user_type)

    @classmethod
    def get_contacts_from_dict(cls, user_dict):
        user_contact = []
        [user_contact.append(cotact) for cotact in user_dict.values()]
        return '|'.join(user_contact)
    
    @classmethod 
    def get_most_common(cls, user_type):
        """
        create tuple with most common types
        takes a dictionary as an argument. 
        """
        result = user_type.split('|')
        result = Counter((",".join(result)).split(','))
        del result[' ']
        return result.most_common()
    
    @classmethod
    def create_user_dict(cls, user_type, user_contact):
        """
        create a dictionary from a string and remove a key-value pair with an empty value
        """
        user_type_list = tuple(user_type[0].split('|'))
        user_contact_list = tuple(user_contact[0].split('|'))
        user_dict = dict(zip(user_type_list, user_contact_list))
        ud = user_dict.copy()
        for key, value in ud.items():
            if not value:
                del user_dict[key]
        return user_dict
    
    @classmethod
    def create_contacts_list(cls, user_contact):
        user_contact_list = tuple(user_contact.split('|'))
        return user_contact_list
