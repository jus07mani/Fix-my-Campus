FixMyCampus
A simple campus maintenance complaint tracker built with Python and Tkinter.

Students can record problems such as a broken fan, leaking tap, or faulty projector. The application keeps a local list of complaints and lets the person using it mark them as resolved.
Features
- Add a complaint with a location and issue description.
- Display pending and resolved complaints.
- Mark a selected complaint as resolved.
- Show the number of pending and resolved complaints.
- Save complaints locally and load them when the app opens.
- Simple white interface with olive-green buttons.
Requirements
- Python 3 with Tkinter support.
- A desktop environment to display the window.
The program uses tkinter, json, and os from Python's standard library. No pip packages are required. Some Linux Python installations require Tkinter to be installed separately.
Run the app
Save the Python code as fix_my_campus.py. Open a terminal in its folder and run:
python fix_my_campus.py
If your system uses python3 instead:
python3 fix_my_campus.py
How to use
1. Enter a location, such as Block A, Room 203.
2. Describe the issue, such as Projector is not working.
3. Click Add Complaint. The complaint appears as Pending.
4. Select a complaint in the list.
5. Click Mark Resolved when the issue has been fixed.
Use the horizontal scrollbar to read long complaint entries. Saved complaints load automatically the next time you open the app.
Files
- fix_my_campus.py — application code.
- complaints.json — local data file created after the first successful save.
- README.md — setup and usage instructions.
- FixMyCampus_Documentation.docx — project description and technical documentation.
How it works
Each complaint contains a location, issue, and status. Complaints are held in a Python list of dictionaries and saved to complaints.json beside the Python script. The app needs permission to write to that folder.
Scope and limitations
This is a classroom prototype running on one computer. It does not send complaints to campus staff or share them across computers. It has no login or access controls; anyone with access to the local data file can read it. There is no edit or delete function.

Avoid uploading real complaint data to GitHub. Add complaints.json and pycache/ to your .gitignore file.

If complaints.json is unreadable or contains invalid JSON, the app shows an error and exits. Back up the file before repairing or removing it. The current version expects the stored data to keep the structure created by the application.
