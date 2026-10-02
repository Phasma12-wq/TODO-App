from todo_tasks import todo_handler

handler = todo_handler()
for i in range(1, 6):
    handler.add_todo(f"Task {i}")
print('List length:', len(handler._todo_list))
result = handler.remove_todo('4')
print('Result:', repr(result))
print('List length after:', len(handler._todo_list))
