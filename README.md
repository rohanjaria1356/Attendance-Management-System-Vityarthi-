Overview:

This project is a simple and interactive GUI-based Attendance Management System built using Python and Tkinter. It enables users to record a student’s Name, Roll Number, Attendance Status (Present/Absent) along with the current Date and Time. The system uses Tkinter’s Treeview widget to present attendance data in a structured table format.

The project also demonstrates core concepts of event-driven programming and GUI state management in Python.

Features:

Add attendance entries (Present/Absent)

Automatic time-stamping using datetime

Display records dynamically in a table

Auto-fill input fields on row selection

Delete selected attendance entries

Automatic table refresh after every update

Clean and interactive interface

Technologies Used:

Python 3.x

Tkinter (Graphical User Interface)

Tkinter ttk (Treeview for tabular display)

Datetime module

How It Works:

1. The user enters the Name and Roll Number.

2. Clicking Present or Absent stores the entry.

3. The system automatically records the date and time.

4. All entries appear in the Treeview table.

5. Selecting a table row loads the details into the input fields.

6. The Delete button removes the selected entry.

All attendance data is temporarily stored in a Python dictionary during the session.

Learning Outcomes:

Understanding Tkinter-based GUI development

Mastery of GUI variable handling (StringVar, IntVar)

Implementation of structured data visualization using Treeview

Development of CRUD operations using Python

Event-driven programming using callbacks and bindings

Real-time UI updates and state management

Use of Python dictionaries for dynamic data storage

Run Instructions:

1. Install Python (if not installed).

2. Tkinter is included by default in standard Python installations.

3. Save the script as attendance.py.

4. Run the project using the command:

     python attendo.py
