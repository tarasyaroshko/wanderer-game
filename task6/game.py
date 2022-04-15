class Street:
    """
    Room class
    """
    def __init__(self, name) -> None:
        """
        Constructor
        """
        self.name = name
        self.linked_rooms = {'1': None, '2': None, '3': None, '4': None, '5': None}
        self.character = None
        self.item = None

    def set_description(self, description):
        """
        Set the description of the room
        """
        self.description = description

    def set_item(self, item):
        """
        Place an item in the room
        """
        self.item = item

    def set_character(self, character):
        """
        Place a character in the room
        """
        self.character = character

    def get_character(self):
        """
        Return the room's character
        """
        return self.character

    def get_item(self):
        """
        Return the room's item
        """
        return self.item

    def link_room(self, room, direction):
        """
        Link room to another room in a given direction
        """
        self.linked_rooms[direction] = room

    def get_details(self):
        """
        Get details of the room
        """
        print("\n")
        print(self.name)
        print("-" * 20)
        print(self.description)
        print("\n")
        print("From here you can go to:")
        for i in self.linked_rooms:
            if self.linked_rooms[i] != None:
                print(f'{i} - {self.linked_rooms[i].name}')
        if self.character != None:
            print(f'{self.character.name} is here!')
        if self.item != None:
            print(f'The [{self.item.name}] is here!')

    def move(self, direction):
        """
        Move to another room in a given direction
        """
        if self.linked_rooms[direction] != None:
            return self.linked_rooms[direction]
        print('\nSeems you got lost... Try another option!')
        return self

class Item:
    """
    Item class
    """
    def __init__(self, name) -> None:
        """
        Constructor
        """
        self.name = name

    def set_description(self, description):
        """
        Set the description of an item
        """
        self.description = description

    def describe(self):
        """
        Print the description of the item
        """
        print(f"The {self.name} is here! - {self.description}")

    def get_name(self):
        """
        Return the item's name
        """
        return self.name


class Character:
    """
    Character class
    """
    def __init__(self, name, description) -> None:
        """
        Constructor
        """
        self.name = name
        self.description = description

    def set_conversation(self, conversation):
        """
        Set the conversation for the character
        """
        self.conversation = conversation

    def talk(self):
        """
        Print what the character says
        """
        print(f"[{self.name} says]: {self.conversation}")

    def describe(self):
        """
        Print the character's description
        """
        print(f"{self.name} is here!")
        print(self.conversation)


class Enemy(Character):
    """
    Character -> Enemy class
    """
    _defeated = 0

    def __init__(self, name, description) -> None:
        """
        Constructor
        """
        super().__init__(name, description)

    def set_weakness(self, weakness):
        """
        Set the enemy's weakness
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        Check if you can fight with the chosen item
        """
        return fight_with == self.weakness

    def get_defeated(self):
        """
        Return the amount of defeated enemies
        """
        self.__class__._defeated += 1
        return self.__class__._defeated


class Friend(Character):
    """
    Character -> Friend class
    """
    def __init__(self, name, description, gift) -> None:
        super().__init__(name, description)
        self.gift = gift
    def gift(self):
        return self.gift
