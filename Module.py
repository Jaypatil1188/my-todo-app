FILEPATH = "todo.txt "

def my_Todos(filepath=FILEPATH):
    """ TEll the Data"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_Todo(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)