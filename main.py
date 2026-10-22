import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")

conn.commit()


tasks = []

while True:
    print("\n======= Task Manager Pro =======")
    print("1. Add Task")
    print("2. View Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task name: ")
        cursor.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
        conn.commit()
        print("Task added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM tasks")
        all_tasks = cursor.fetchall()

        if len(all_tasks) == 0:
            print("No tasks available!")

        else:
            for task in all_tasks:
                print(task[0], ".", task[1])

    elif choice == "3":
        cursor.execute("SELECT id, title FROM tasks")
        all_tasks = cursor.fetchall()

        if len(all_tasks) == 0:
            print("No tasks available")
        else:
            for task in all_tasks:
                print(task[0], ".", task[1])

        task_id = int(input("Enter task ID to edit: "))
        new_title = input("Enter new task name: ")

        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Task updated successfully!")
        else:
            print("Invalid task ID")

    elif choice == "4":
        cursor.execute("SELECT * FROM tasks")
        all_tasks = cursor.fetchall()

        if len(all_tasks) == 0:
            print("No tasks available!")

        else:
            for task in all_tasks:
                print(task[0], ".", task[1])

            task_number = int(input("Enter task number to delete : "))

            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_number,))
            conn.commit()
        
        if cursor.rowcount > 0:
            print("Task deleted successfully!")

        else:
            print("Invalid Task Number")

    elif choice == "5":
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
