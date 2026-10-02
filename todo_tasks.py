from data_classes import todo_item, todo

"""
    This section handles function calls from the frontend
"""
class todo_handler:
    def __init__(self):
        self._todo_list: list[todo] = []
        pass

    def display_menu(self,menu_items):
            for i in range(len(menu_items)):
                print(f"{i+1}. {menu_items[i]}")
            print('')

    def display_list(self):
            if len(self._todo_list) > 0 :
                for i in range(len(self._todo_list)):
                    print(f"{i+1}. {self._todo_list[i].getStr()}")
                print('')
            else:
                print("<list is empty>")
                print('')

    def isNotEmpty(self):
        return len(self._todo_list) > 0
    
    def add_todo(self, name):
        if name == None or name == '':
            return  "Input must be provided"
     
        self._todo_list.append(todo_item(name))

        return "TODO added to list"

    def remove_todo(self, value):
        try:
            index = int(value)-1
        except ValueError:
            return "input must a valid number"

        if not self.isInRange(index):
            return f"number must be within list index range (1-{len(self._todo_list)})"

        del self._todo_list[index]
        return "TODO removed to list" 

    def markAsDone(self, value):
        try:
            index = int(value)-1
        except ValueError:
            return "input must a valid number"
        
        if not self.isInRange(index):
            return f"number must be within list index range (1-{len(self._todo_list)})"

        self._todo_list[index].markDone()

        return f"{self._todo_list[index].name} marked as done"

    def isInRange(self, index):
        return True if index >= 0 and index < len(self._todo_list) else False


"""
    helper functions
    - is in range
"""