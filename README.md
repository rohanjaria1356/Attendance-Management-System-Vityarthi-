Overview:-

A simple and interactive GUI-based Attendance Management System built using Python and Tkinter. It allows users to record a student’s Name, Roll Number, Attendance Status (Present/Absent), along with the current Date and Time. The system uses Tkinter’s Treeview widget to display attendance data in a structured table format.

The project demonstrates core concepts of event-driven programming and GUI state management in Python.

Features:-

1. Add attendance entries (Present/Absent)
2. Automatic time-stamping using datetime
3. Display records dynamically in a table
4. Auto-fill input fields on row selection
5. Delete selected attendance entries
6. Automatic table refresh after every update
7. Clean and interactive interface
   
Objectives:-

1. Understanding Tkinter-based GUI development
2. Mastery of GUI variable handling (StringVar, IntVar)
3. Implementation of structured data visualization using Treeview
4. Development of CRUD operations using Python
5. Event-driven programming using callbacks and bindings
6. Real-time UI updates and state management
7. Use of Python dictionaries for dynamic data storage
   
Technologies Used:-

1. Python 3.x
2. Tkinter (Graphical User Interface)
3. Tkinter ttk (Treeview for tabular display)
4. Datetime module
(No external packages required.)

Project Structure:-

attendance_management/ ├─ attendance.py # Main script containing the GUI application └─ README.md

Installation & Running:-

Using PyCharm-

1. Open this project folder in PyCharm
2. Open attendance.py
3. Click Run
   
Using Command Line-

1. Install Python (if not installed).
2. Tkinter is included by default in standard Python installations.
3. Save the script as attendance.py.
4. Run: python attendance.py
   
Example Usage:-

1. Launch the application.
2. Enter the student's Name and Roll Number in the input fields.
3. Click "Present" or "Absent" to record the attendance.
4. The entry appears in the table with automatic date and time.
5. Select a row in the table to auto-fill the input fields.
6. Click "Delete" to remove the selected entry.
   
Storage Format:-

All attendance data is temporarily stored in a Python dictionary during the session. Each entry includes:

* Name
* Roll Number
* Status (Present/Absent)
* Date and Time (auto-generated)
  
Data is not persisted across sessions; it resets when the application closes.

Architecture:-

GUI Layer (Tkinter) ↓ Event Handlers (Callbacks) ↓ Data Layer (Python Dictionary)

Functional Modules:-

* Attendance entry addition (Present/Absent)
* Automatic time-stamping
* Dynamic table display and refresh
* Row selection and auto-fill
* Entry deletion
* Input validation and state management

Non-Functional Requirements:-

| Requirement | Implementation |
|-------------|--------------------|
| Usability | Intuitive GUI with buttons, inputs, and table for easy interaction |
| Reliability | Safe operations with automatic refreshes and error-free deletions |
| Maintainability | Code organized in a single script with clear functions |
| Efficiency | Minimal resource usage for a lightweight GUI app |
| Error Handling | Basic input checks and safe dictionary operations |
| Auditability | Records include timestamps for each attendance entry |


-------
