# Task 1 - Student Assignment Manager

## Overview
This folder contains **Task 1** of the COMP8090SEF individual course project.

The project is a Python command-line application called **Student Assignment Manager**.  
It is designed to help students manage academic tasks such as assignments, exams, and general study tasks in a clear and structured way.

This task focuses on applying **object-oriented programming** and **modular programming** to solve a real-life problem.

## Main Features
- Add a new task
- View all tasks
- Search tasks by keyword
- Filter tasks by course
- Sort tasks by due date
- Toggle completion status
- Delete a task
- Save task data to a file

## OOP Design
The system uses the following object-oriented structure:

- **Task**: base class
- **AssignmentTask**: subclass for assignment-related tasks
- **ExamTask**: subclass for exam-related tasks
- **GeneralTask**: subclass for general study tasks
- **TaskManager**: manages all tasks
- **Storage module**: handles saving and loading data

This design demonstrates:
- Inheritance
- Polymorphism
- Encapsulation
- Modular programming

## File Structure
- `main.py` - main program and command-line interface
- `models.py` - task classes
- `manager.py` - task management logic
- `storage.py` - file storage logic
- `USER_GUIDE.md` - user guide

## How to Run
Open a terminal in the project root directory and run:

```bash
python -m task1.main
