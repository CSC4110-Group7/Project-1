#CSC 4110 Project 3 - Team 7 TM
#BEGIN
"""
Objectives:
1.) Create a mock application that does something
2.) Application must store information
3.) Application must forward information
4.) Include a UI
5.) Include EULA on startup
6.) Include docstrings
7.) Make sure code can't be executed if imported.
"""
"""
Solution plan: Make an 'affirmation tracker'
1.) Affirmation Tracker will store affirmation and date affirmed
2.) Affirmation tracker will be able to search affirmation
by affirmation content or affirmation date
3.) TKinter UI
4.) Tkinter startup that contains 
mandatory EULA, which on accepting
opens main TKINTER window
5.) Uses docstrings (look this comment is in a docstring, haha)
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

def open_new_window():
    root.withdraw()  # Hide the initial EULA window in hindsight I shouldn't have named this root.
    tracker_window.deiconify()   # Show the main affirmation tracker window which has a different name

#This function saves the affirmation to the CSV
def save_affirmation():
    #get the text from the textbox
    affirmation_text = affirmation_entry.get("1.0", tk.END).strip()
    #if the text exists,save it, otherwise DON'T
    if affirmation_text:
        #get the timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("affirmations.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, affirmation_text])
        messagebox.showinfo("Success", "Affirmation saved successfully.")
        #Clean up the affirmation entry box so that user doesn't put duplicates in ME - I HAVE DONE THAT
        affirmation_entry.delete("1.0", tk.END)
    else:
        messagebox.showerror("Error", "Please enter an affirmation.")

#Generic display everything button
def display_all_affirmations():
    #use try catch loop because there's a chance the user hasn't put ANYTHING in. Yeah. Great job.
    try:
        #open the file, show everything
        with open("affirmations.csv", "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            display_text = ""
            for row in data:
                display_text += f"Timestamp: {row[0]}, Affirmation: {row[1]}\n\n"
            display_text = display_text.strip()
            display_textbox.delete("1.0", tk.END)
            display_textbox.insert("1.0", display_text)
    except FileNotFoundError:
        messagebox.showerror("Error", "No affirmations found.")

#Search function
def search_affirmations():
    search_query = search_entry.get().strip().lower()
    try:
        #CSV reader - reads the csv, converts it in a list, and for each row in the [1] category dedicated
        #to the string for affirmation search for it. 
        with open("affirmations.csv", "r") as file:
            reader = csv.reader(file)
            data = list(reader)
            display_text = ""
            for row in data:
                #if there is a match, slap it into the messagebox using a big string
                if search_query.lower() in row[1].lower() or search_query.lower() in row[0].lower():
                    display_text += f"Timestamp: {row[0]}, Affirmation: {row[1]}\n\n"
            if not display_text:
                display_text = "No matching affirmations found."
            #Put everything in the textbox using the string we built
            display_textbox.delete("1.0", tk.END)
            display_textbox.insert("1.0", display_text)
    except FileNotFoundError:
        messagebox.showerror("Error", "No affirmations found.")
        
#chastise the user for attempting to close without accepting.
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit? You could just accept the license agreement - just saying"):
        root.destroy()

# Main window
root = tk.Tk()
root.title("End User License Agreement")

# EULA Text (Lorum Ipsum)
eula_text = """
By using this software you agree not to sell or distribute 
data without the express consent of Forestview 
You hereby indemnify Forestview from all legal ramnifications 
regarding data breaches, zero-day attacks, and database worms. 
Vendors are required to make periodic vulnerability 
assessments of this system. This agreement is subject 
to change, and will change to stay accurate with the 
current security and technology climate
"""

# Display EULA Text
eula_label = tk.Label(root, text=eula_text, wraplength=400, justify="left")
eula_label.pack(padx=10, pady=10)

# Accept Button
accept_button = tk.Button(root, text="Accept", command=open_new_window)
accept_button.pack(pady=10)

#Use the closing of the window to trigger a messagebox asking not to do that.
root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle window closing event I had an error where the 
#x button didn't close the program, and due to my poorly structured code would lead to the tracker launching anyway
#This complicated silly solution makes it work instead.







# Create affirmation tracker window
tracker_window = tk.Toplevel(root)
tracker_window.title("Forestview Affirmation Tracker")
tracker_window.withdraw()  # Hide the tracker window initially, we will show it using deiconfiy

# Tab control
tab_control = ttk.Notebook(tracker_window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="New Affirmation")
tab_control.add(tab2, text="Display/Search Affirmations")
tab_control.pack(expand=1, fill="both")

# Tab 1: New Affirmation
affirmation_label = tk.Label(tab1, text="Enter Affirmation:")
affirmation_label.pack(pady=5)

affirmation_entry = tk.Text(tab1, height=5, width=50)
affirmation_entry.pack(pady=5)

save_button = tk.Button(tab1, text="Save", command=save_affirmation)
save_button.pack(pady=5)

# Tab 2: Display/Search Affirmations
search_label = tk.Label(tab2, text="Search Affirmations by Text:")
search_label.pack(pady=5)

search_entry = tk.Entry(tab2, width=50)
search_entry.pack(pady=5)

search_button = tk.Button(tab2, text="Search", command=search_affirmations)
search_button.pack(pady=5)

display_button = tk.Button(tab2, text="Display All", command=display_all_affirmations)
display_button.pack(pady=5)

display_textbox = tk.Text(tab2, height=15, width=50)
display_textbox.pack(pady=5)

root.mainloop()
#END