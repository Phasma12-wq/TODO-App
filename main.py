from todo_app import TODO_app
from todo_tasks import todo_handler
"""
    This section creates the instance of the app and its associated dependencies to start the todo list app
"""
def main():
    print("Welcome to the TODO List App")
    menu_items: tuple = ("[A]dd","[M]ark done","[R]emove","[E]xit")
    function_handler = todo_handler()

    app = TODO_app(menu_items, function_handler)

    try:
        app.start()
    except KeyboardInterrupt:
            print("\nProcess interrupted by user.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    finally:
        print("Exiting program.")

"""
    Menu display
    1. Add
    2. Remove
    3. Exit

    functions
    1. display menu
    2. display todo list
"""

