
import os
"""
    This section handles frontend interaction with user
"""
class TODO_app:
    def __init__(self, menu_items, handler):
        self._menu_items = menu_items
        self._handler = handler

    def start(self):
        while True:
            os.system("clear")

            self._handler.display_list()
            self._handler.display_menu(self._menu_items)
    
            user_input = input("Enter option (A,M,R,E): ")

            match(str.upper(user_input)):
                case 'A':
                    self.__add()
                case 'M':
                    self.__markDone()
                case 'R':
                    self.__remove()
                case 'E':
                    return
                case _:
                    print("invalid option")
            input('')

    def __add(self):
        user_input = input("Provide a TODO name: ")
        output = self._handler.add_todo(user_input)
        print(output)
        return

    def __remove(self):
        if not self._handler.isNotEmpty():
            print("list is empty")
            return

        print("Choose what todo item you want to remove:")
        self._handler.display_list()
        
        user_input = input("Provide a TODO list number: ")
        output = self._handler.remove_todo(user_input)
        print(output) 
        return

    def __markDone(self):
        if not self._handler.isNotEmpty():
            print("list is empty")
            return

        print("Choose what todo item you want to mark as Done:")
        self._handler.display_list()

        user_input = input("Provide a TODO list number: ")
        output = self._handler.markAsDone(user_input)
        print(output)
        return