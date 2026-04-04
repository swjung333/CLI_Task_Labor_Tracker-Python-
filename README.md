# CLI_Task_Labor_Tracker-Python-
A Python Command-Line Interface (CLI) tool for managing tasks and tracking labor hours with real-time validation.


## Project Overview
This CLI Task Management System is a lightweight productivity tool designed for high-efficiency labor tracking. Built with Python, it allows users to manage complex task lifecycles while providing a robust engine for calculating precise work durations using 24-hour time logic.

---

## Key Features
Dynamic Task Lifecycle Management: Full CRUD (Create, Read, Update, Delete) functionality allowing users to add, search, rename, and remove tasks on the fly.

Intelligent Labor Hour Calculation: * Accepts HH:MM 24-hour format inputs.

Midnight Rollover Logic: Automatically detects and adjusts calculations for shifts that cross over 12:00 AM (e.g., a task starting at 11:00 PM and ending at 1:00 AM is correctly calculated as 2 hours).

Data Integrity & Validation: * Prevents duplicate task entries.

Strict error handling for invalid time ranges (00:00–23:59).

Ensures status and duration lists remain synchronized with the primary task list.

Productivity Analytics: A details reporting engine that aggregates completion rates and calculates total cumulative labor hours for the entire session.

---

