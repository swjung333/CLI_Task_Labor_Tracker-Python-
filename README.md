# CLI_Task_Labor_Tracker-Python-
A Python Command-Line Interface (CLI) tool for managing tasks and tracking labor hours with real-time validation.


## Project Overview
This CLI Task Management System is a lightweight productivity tool designed for high-efficiency labor tracking. Built with Python, it allows users to manage complex task lifecycles while providing a robust engine for calculating precise work durations using 24-hour time logic.

This project was developed as part of a university final assessment ('Python'), emphasizing practical software design, time computation logic, and CLI-based system architecture.

---

## Key Features
Dynamic Task Lifecycle Management: Full CRUD (Create, Read, Update, Delete) functionality allowing users to add, search, rename, and remove tasks on the fly.

Intelligent Labor Hour Calculation: *Accepts HH:MM 24-hour format inputs*.

Midnight Rollover Logic: Automatically detects and adjusts calculations for shifts that cross over 12:00 AM (e.g., a task starting at 11:00 PM and ending at 1:00 AM is correctly calculated as 2 hours).

Data Integrity & Validation: *Prevents duplicate task entries*.

Strict error handling for invalid time ranges (00:00–23:59).

Ensures status and duration lists remain synchronized with the primary task list.

Productivity Analytics: A details reporting engine that aggregates completion rates and calculates total cumulative labor hours for the entire session.

---

## Technical Implementation 

### Architecture
The system uses a **parallel list structure** to manage task state:

- `task_names` -> task identifiers  
- `task_statuses` -> completion state (True/False)  
- `task_durations` -> recorded work hours 

This ensures synchronized state management across all operations.

### Core Logic: Time Calculation

The program is designed to avoid external libraries for the project and implements manual time computation instead:

1. Convert input time into total minutes  
2. Compute difference between start and end  
3. Handle overnight tasks using 24-hour adjustment

Formula used:
TotalTime = (EndMinutes - StartMinutes + 1440) % 1440
**This guarantees correct results even when tasks cross midnight.**

Example:

Enter command: add
Enter a new task name: EDA #1
Task added successfully.

Enter command: done
Enter a task name to complete: EDA #1
Start time: 22:30
End time: 01:15
Task marked as done. Duration: 2.75 hours

---

## Example Commands
add -> create a task
view -> list all tasks
edit -> rename a task
remove -> delete a task
search -> find a task
done -> mark task complete + log time
details -> show summary statistics
exit -> quit program

---

## Skills Demonstrated

- Python fundamentals (control flow, lists, loops)
- Input validation and error handling
- Algorithmic thinking (time normalization logic)
- CLI application design
- Data consistency management
