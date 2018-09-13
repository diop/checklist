todos = list()

def create(task):
    todos.append(task)

def read(index):
    return todos[index]

def update(index, task):
    todos[index] = task

def destroy(index):
    todos.pop(index)

def list_all_tasks():
    index = 0
    for task in todos:
        print("{} {}".format(index, task))
        index += 1

def mark_completed(index):
    task = todos[index]
    todos[index] = "√" + task

def select(function_code):

    if function_code == "C":
        input_task = user_input("Input task: ")
        create(input_task)
    elif function_code == "R":
        task_index = user_input("Index number? ")
        read(task_index)
    elif function_code == "P":
        list_all_tasks()
    elif function_code == "Q":
        return False
    else:
        print("Option unknown")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    create("task one")
    create("task two")
    print(read(0))
    print(read(1))

    update(0, "task three")

    destroy(1)

    mark_completed(0)
    print(read(0))

    user_value = user_input("Please enter a value: ")
    print(user_value)

    select("C")
    list_all_tasks()
    select("R")

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list of tasks, R to read from list and P to display list..."
    )
    running = select(selection)
