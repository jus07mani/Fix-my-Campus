import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("FixMyCampus")
root.geometry("720x600")
root.configure(bg="white")

olive = "#556B2F"
data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "complaints.json")
complaints = []


def show_complaints():
    complaint_list.delete(0, tk.END)
    pending = 0

    for item in complaints:
        text = item["status"] + " | " + item["location"] + " | " + item["issue"]
        complaint_list.insert(tk.END, text)
        if item["status"] == "Pending":
            pending += 1

    resolved = len(complaints) - pending
    counter.config(text=f"{pending} pending  •  {resolved} resolved")


def save_complaints():
    try:
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump(complaints, file, indent=4)
        return True
    except OSError:
        messagebox.showerror("Save error", "Could not save the complaints.")
        return False


def add_complaint():
    place = location.get().strip()
    problem = issue.get("1.0", tk.END).strip()

    if place == "" or problem == "":
        messagebox.showwarning("Missing details", "Enter the location and issue.")
        return

    complaints.append({
        "location": place,
        "issue": problem.replace("\n", " "),
        "status": "Pending"
    })

    if not save_complaints():
        complaints.pop()
        return

    show_complaints()
    location.delete(0, tk.END)
    issue.delete("1.0", tk.END)
    location.focus_set()


def mark_resolved():
    selected = complaint_list.curselection()

    if not selected:
        messagebox.showwarning("Select a complaint", "Select a complaint first.")
        return

    index = selected[0]
    old_status = complaints[index]["status"]
    complaints[index]["status"] = "Resolved"

    if not save_complaints():
        complaints[index]["status"] = old_status
        return

    show_complaints()
    complaint_list.selection_set(index)


tk.Label(root, text="FixMyCampus", font=("Arial", 24, "bold"),
         bg="white", fg=olive).pack(pady=(20, 5))

tk.Label(root, text="Report a problem. Track the fix.",
         font=("Arial", 11), bg="white", fg="#666666").pack(pady=(0, 15))

tk.Label(root, text="Location", font=("Arial", 11, "bold"),
         bg="white", fg=olive).pack(anchor="w", padx=25)

location = tk.Entry(root, font=("Arial", 12), relief=tk.SOLID, bd=1)
location.pack(fill=tk.X, padx=25, pady=(5, 12))

tk.Label(root, text="Describe the issue", font=("Arial", 11, "bold"),
         bg="white", fg=olive).pack(anchor="w", padx=25)

issue = tk.Text(root, height=3, font=("Arial", 11),
                wrap="word", relief=tk.SOLID, bd=1)
issue.pack(fill=tk.X, padx=25, pady=5)

tk.Button(root, text="Add Complaint", command=add_complaint,
          bg=olive, fg="white", font=("Arial", 11),
          relief=tk.FLAT, width=20, pady=7).pack(pady=12)

tk.Label(root, text="Campus complaints", font=("Arial", 12, "bold"),
         bg="white", fg=olive).pack(anchor="w", padx=25)

complaint_list = tk.Listbox(root, font=("Arial", 11), height=8,
                           bg="#F5F7EF", selectbackground=olive,
                           selectforeground="white", activestyle="none")
complaint_list.pack(fill=tk.BOTH, expand=True, padx=25, pady=(8, 0))

scroll = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=complaint_list.xview)
scroll.pack(fill=tk.X, padx=25)
complaint_list.config(xscrollcommand=scroll.set)

tk.Button(root, text="Mark Resolved", command=mark_resolved,
          bg=olive, fg="white", font=("Arial", 11),
          relief=tk.FLAT, width=20, pady=7).pack(pady=12)

counter = tk.Label(root, text="", font=("Arial", 11, "bold"),
                   bg="white", fg=olive)
counter.pack(pady=(0, 15))

try:
    with open(data_file, "r", encoding="utf-8") as file:
        complaints = json.load(file)
except FileNotFoundError:
    complaints = []
except (OSError, ValueError):
    messagebox.showerror("Open error", "Could not read complaints.json.")
    root.destroy()
    raise SystemExit

show_complaints()
root.mainloop()