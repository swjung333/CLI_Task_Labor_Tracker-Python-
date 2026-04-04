task_names = []
task_statuses = []
task_durations = []

def display_help():
    print("Command Help")
    print("view     : Display all tasks and progress")
    print("add      : Add a new task to the list")
    print("remove   : delete a task from the list")
    print("edit     : change the name of an existing task")
    print("search   : find a task and see its details")
    print("done     : mark a task as done and record time (HH:MM)")
    print("details  : show summary of all tasks in detail")
    print("exit     : close the program")

for i in range(200):
    user_input = input("Enter command (type 'help' for info): ").strip().lower()

    if user_input == "exit":
        print("Exiting the program. Goodbye!")
        break

    elif user_input == "help":
        display_help()
    
    elif user_input == "view":
        print("Current Tasks")
        for i in range(len(task_names)):
            if task_statuses[i] == True:
                status = "Done"
            else:
                status = "Undone"
            if task_durations[i] == None:
                duration = "N/A"
            else:
                duration = "{} hrs".format(task_durations[i])
            print("Task: {}, Status: {}, Duration: {}".format(task_names[i], status, duration))

    elif user_input == "add":
        name = input("Enter a new task name: ").strip()
        if name in task_names:
            print("Error: Task name already exist.")
        else:
            task_names.append(name)
            task_statuses.append(False)
            task_durations.append(None)
            print("Task added successfully.")

    elif user_input == "remove":
        name = input("Enter a name of task to remove: ").strip()
        if name in task_names:
            idx = task_names.index(name)
            task_names.pop(idx)
            task_statuses.pop(idx)
            task_durations.pop(idx)
            print("Task removed successfully.")
        else:
            print("Error: Task not found.")
            
    elif user_input == "edit":
        old_name = input("Enter a name of task to edit: ").strip()
        if old_name in task_names:
            new_name = input("Enter new name: ").strip()
            if new_name in task_names:
                print("Error: New name already exists.")
            else:
                idx = task_names.index(old_name)
                task_names[idx] = new_name
                print("Task renamed successfully.")
        else:
            print("Error: Task not found.")
        
    elif user_input == "search":
        name = input("Search task: ").strip()
        if name in task_names:
            idx = task_names.index(name)
            if task_statuses[idx] == True:
                status = "Done"
            else:
                status = "Undone"
            if task_durations[idx] is not None:
                period = task_durations[idx]
            else:
                period = "N/A"
            print("Result -> Task: {}, Status: {}, Duration: {}".format(task_names[idx], status, period))
        else:
            print("Error: Task not found.")

    elif user_input == "done":
        name = input("Enter a task name to complete: ").strip()
        if name in task_names:
            idx = task_names.index(name)
            print("Enter time in HH:MM format (24h clock)")
            start_str = input("Start time: ")
            end_str = input("End time: ")

            if ":" not in start_str or ":" not in end_str:
                print("Wrong. Use right time format (e.g., 14:30).")
            else:
                start_time = start_str.split(":")
                end_time = end_str.split(":")
                
                s_hrs = int(start_time[0])
                s_min = int(start_time[1])
                e_hrs = int(end_time[0])
                e_min = int(end_time[1])

                if s_hrs < 0 or s_hrs > 23 or e_hrs < 0 or e_hrs > 23 or s_min < 0 or s_min > 59 or e_min < 0 or e_min > 59:
                    print("Error: Invalid clock time. Use 00:00 to 23:59.")

                else:
                    start_total = (s_hrs * 60) + s_min
                    end_total = (e_hrs * 60) + e_min

                    total_time = end_total - start_total
                    
                    if total_time < 0:
                        total_time = total_time + (24 * 60)

                    task_durations[idx] = total_time/60
                    task_statuses[idx] = True
                    print("Task marked as done. Duration: {} hours".format(task_durations[idx]))
        else:
            print("Error: Task not found.")

    elif user_input == "details":
        total = len(task_names)
        completed = task_statuses.count(True)
        uncompleted = task_statuses.count(False)

        total_hours = 0
        for hr in task_durations:
            if hr is not None:
                total_hours = total_hours + hr

        print("Details")
        print("Total tasks: {}".format(total))
        print("completed: {}".format(completed))
        print("Uncompleted: {}".format(uncompleted))
        print("Total hours worked: {} hrs".format(total_hours))
        
    else:
        print("Unknown command. Type 'help' for a list of commands.")
