from tkinter import *
from Project2Logic import *

class GUI:
    def __init__(self, window):
        """This function initializes the creation of the first window."""
        self.window = window
        self.create_window()

    def create_window(self):
        """This function creates the first window."""
        self.window.geometry("300x325")
        self.window.resizable(False, False)
        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text="Task List Creator", font=("Arial", 20))
        self.label_title.pack(pady=5)
        self.frame_title.pack(pady=5)

        self.frame_task = Frame(self.window)
        self.label_task = Label(self.frame_task, text="Task:", font=("Arial", 13))
        self.input_task = Entry(self.frame_task)
        self.label_task.pack(side='left', padx=5)
        self.input_task.pack(side='left',padx=5)
        self.frame_task.pack(anchor='w', padx=25, pady=5)

        self.frame_deadline = Frame(self.window)
        self.label_deadline = Label(self.frame_deadline, text="Date", font=("Arial", 17))
        self.label_deadline.pack()
        self.frame_deadline.pack()

        self.frame_month = Frame(self.window)
        self.label_month = Label(self.frame_month, text="Month (#):", font=("Arial", 13))
        self.input_month = Entry(self.frame_month)
        self.label_month.pack(side='left', padx=5)
        self.input_month.pack(side='left', padx=5)
        self.frame_month.pack(anchor='w', padx=25, pady=5)

        self.frame_day = Frame(self.window)
        self.label_day = Label(self.frame_day, text="Day (#):", font=("Arial", 13))
        self.input_day = Entry(self.frame_day)
        self.label_day.pack(side='left', padx=5)
        self.input_day.pack(side='left', padx=5)
        self.frame_day.pack(anchor='w', padx=25, pady=5)

        self.frame_year = Frame(self.window)
        self.label_year = Label(self.frame_year, text="Year (#):", font=("Arial", 13))
        self.input_year = Entry(self.frame_year)
        self.label_year.pack(side='left', padx=5)
        self.input_year.pack(side='left', padx=5)
        self.frame_year.pack(anchor='w', padx=25, pady=5)

        self.button_save = Button(self.window, text="Save Task", command=self.append_input)
        self.button_save.pack()

        self.button_done = Button(self.window, text="Done", command=self.task_destroy)
        self.button_done.pack()

        self.error_frame = Frame(self.window)
        self.error_label = Label(self.error_frame, text="Fill all boxes.", fg='gray', font=("Arial", 11))
        self.error_frame.pack(pady=3)
        self.error_label.pack(pady=3)

        self.validate = Validity_check()
        self.csv_handle = CSV_file()

    def return_window(self):
        """This function returns you to the first window."""
        for widget in self.window.winfo_children(): # used Google
            widget.destroy()
        self.create_window()
        self.window.update_idletasks() # used Google because Mac tasks go idle when creating new window

    def task_check(self):
        """This function checks if task name is valid."""
        task = self.input_task.get().strip()
        if self.validate.valid_task(task) is False:
            self.error_label.config(text="Please enter a task.")
            return False
        return True

    def date_check(self):
        """This function checks if date input is valid."""
        month_string = self.input_month.get().strip()
        day_string = self.input_day.get().strip()
        year_string = self.input_year.get().strip()
        valid_check, message = self.validate.valid_date(month_string, day_string, year_string)
        if valid_check is False:
            self.error_label.config(text=message)
            return False
        return True

    def append_input(self):
        """This function appends input to the CSV file."""
        task_check = self.task_check()
        date_check = self.date_check()
        if task_check is False or date_check is False:
            return
        else:
            self.csv_handle.save_to_csv(self.input_task.get().strip(), self.input_month.get().strip(), self.input_day.get().strip(), self.input_year.get().strip())
            self.input_task.delete(0, END)
            self.input_month.delete(0, END)
            self.input_day.delete(0, END)
            self.input_year.delete(0, END)
            self.input_task.focus()
            self.error_label.config(text="Fill all boxes.")

    def task_destroy(self):
        """This function destroys the first window."""
        for widget in self.window.winfo_children():
            widget.destroy()
        self.new_window()

    def remove_task(self, task_to_remove):
        """This function removes the chosen task from the CSV file and refreshes the list."""
        self.csv_handle.remove_from_csv(task_to_remove)
        self.task_destroy()

    def button_remove_task(self, event):
        """This function removes the task linked to the remove button."""
        task_to_remove = event.widget.task_data # used AI for this line
        self.remove_task(task_to_remove)

    def new_window(self):
        """This function creates the second window."""
        self.window.geometry("300x325")
        self.window.resizable(True, True)
        self.frame_all_tasks = Frame(self.window)
        self.label_all_tasks = Label(self.frame_all_tasks, text="Your Tasks:", font=("Arial", 20))
        self.frame_all_tasks.pack()
        self.label_all_tasks.pack()
        with open('tasks.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                task_name, month, day, year = row
                self.frame_final_task = Frame(self.window)
                self.label_final_task = Label(self.frame_final_task, text=f'{task_name} (Date: {month}/{day}/{year})')

                self.label_final_task.pack(side='left')
                self.frame_final_task.pack()
                self.button_remove = Button(self.frame_final_task, text="Remove", command=lambda task=row: self.remove_task(task))
                self.button_remove.pack(side='right')
                self.button_remove.task_data = row
                self.button_remove.bind("<Button-1>", self.button_remove_task) # used AI for this line


        self.button_return = Button(self.window, text="Return", command=self.return_window)
        self.button_return.pack()
