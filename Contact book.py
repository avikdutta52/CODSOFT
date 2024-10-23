import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Function to handle Add, Update, Delete, and Search operations
def manage_contact(action):
    name, phone, email, address = name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()
    
    if action == 'add':
        if name in contacts:
            messagebox.showerror("Error", "Contact already exists!")
        else:
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact {name} added!")
    
    elif action == 'update':
        if name in contacts:
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact {name} updated!")
        else:
            messagebox.showerror("Error", "Contact does not exist!")
    
    elif action == 'delete':
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted!")
        else:
            messagebox.showerror("Error", "Contact does not exist!")

    elif action == 'search':
        contact_list.delete(0, tk.END)
        for contact_name, details in contacts.items():
            if name.lower() in contact_name.lower() or phone in details["Phone"]:
                contact_list.insert(tk.END, f"{contact_name}: {details['Phone']}")
        if not contact_list.size():
            messagebox.showinfo("Info", "No contact found.")
    
    clear_fields()

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['Phone']}")

# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Contact Manager")

# Labels and Entry fields for contact details
for idx, label in enumerate(["Name:", "Phone:", "Email:", "Address:"]):
    tk.Label(root, text=label).grid(row=idx, column=0)

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)
entries = [name_entry, phone_entry, email_entry, address_entry]
for idx, entry in enumerate(entries):
    entry.grid(row=idx, column=1)

# Listbox to display contacts
contact_list = tk.Listbox(root, height=10, width=50)
contact_list.grid(row=7, column=0, columnspan=2)

# Buttons for actions
actions = [("Add Contact", "add"), ("View Contacts", "view"), ("Search", "search"), 
           ("Update Contact", "update"), ("Delete Contact", "delete")]
for idx, (text, action) in enumerate(actions):
    if action == "view":
        tk.Button(root, text=text, command=view_contacts).grid(row=4+idx//2, column=idx%2)
    else:
        tk.Button(root, text=text, command=lambda a=action: manage_contact(a)).grid(row=4+idx//2, column=idx%2)

# Run the UI
root.mainloop()
