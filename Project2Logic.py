import csv
class Validity_check():
    def __init__(self):
        self.filename = 'tasks.csv'
    def valid_task(self, task: str) -> bool:
        """This function checks if the task is valid.
        :param task: The task to be checked.
        """
        if task.strip() == '':
            return False
        else:
            return True

    def valid_date(self, month_string: str, day_string: str, year_string: str) -> tuple[bool, str]:
        """This function checks if the date is valid.
        :param month_string: The month to be checked.
        :param day_string: The day to be checked.
        :param year_string: The year to be checked.
        """
        if month_string == '' or day_string == '' or year_string == '':
            return False, "All date boxes must be filled."
        try:
            month = int(month_string)
            day = int(day_string)
            year = int(year_string)
        except ValueError:
            return False, "Date must be a number."
        if month < 1 or month > 12:
            return False, "Month must be valid."
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day < 1 or day > 29:
                    return False, "Day must be valid."
            else:
                if day < 1 or day > 28:
                    return False, "Day must be valid."
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                return False, "Day must be valid."
        if len(year_string) != 4:
            return False, "Year must be valid."
        return True, ""

class CSV_file():
    def __init__(self):
        self.filename = 'tasks.csv'
    def save_to_csv(self, task: str, month: str, day: str, year: str, filename='tasks.csv') -> None:
        """This function saves a task to a csv file.
        :param task: The task to be saved.
        :param month: The month to be saved.
        :param day: The day to be saved.
        :param year: The year to be saved.
        :param filename: The name of the csv file.
        """
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([task, month, day, year])

    def load_from_csv(self, filename: str) -> list:
        """This function loads the task from the csv file.
        :param filename: The name of the csv file.
        """
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)

    def remove_from_csv(self, task_to_remove: list, filename='tasks.csv') -> None:
        """This function removes the task from the csv file.
        :param task_to_remove: The task to be removed.
        :param filename: The name of the csv file.
        """
        tasks = []
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if row != task_to_remove:
                    tasks.append(row)
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(tasks)
