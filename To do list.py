tasks = []

def display_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']} [{'Done' if task['status'] else 'Not Done'}]")

def add_task():
    tasks.append({"name": input("Enter a new task: "), "status": False})

def mark_done():
    display_tasks()
    if tasks:
        tasks[int(input("Task number to mark as done: ")) - 1]['status'] = True

def remove_task():
    display_tasks()
    if tasks:
        tasks.pop(int(input("Task number to remove: ")) - 1)

while True:
    action = input("\n1. View Tasks  2. Add Task  3. Mark Done  4. Remove  5. Exit\nChoose: ")
    if action == '1': display_tasks()
    elif action == '2': add_task()
    elif action == '3': mark_done()
    elif action == '4': remove_task()
    elif action == '5': break
    else: print("Invalid choice.")
