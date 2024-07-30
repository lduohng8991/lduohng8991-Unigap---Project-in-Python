import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

import logging # for more robust to traceback (INFO: to see the result in this case)

TASKS_FILE = "tasks.json"

#def calculate_completion_rate(tasks):
'''
    Return percent of completed task
'''
def calculate_completion_rate(tasks):
    # Handling Error when open a file with try & except
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
    
        all_tasks = len(tasks['tasks']) # count the total of tasks existed
        completed_tasks = sum(task['completed'] == True for task in tasks['tasks']) # count tasks based on our criteria
        completion_rate = 0  # rate, firstly was 0

        if all_tasks > 0:
            completion_rate  = round((completed_tasks / all_tasks), 2) 
        # final results when first percent(0) different with actual percent
        else: 
            0.00
        
        return completion_rate  
    
    except FileNotFoundError:
        print("Your file {TASK_FILE} was not found!")
        # default None in return

####################

#def analyze_task_distribution(tasks):
    '''
    Return number of task distribute by category
    '''
# for counting
from collections import Counter

logging.basicConfig(level = logging.INFO, 
                    format = '%(asctime)s %(created)f %(funcName)s %(lineno)d %(message)s') # Log expected

def analyze_task_distribution(tasks):
    # Handling Error when open a file with try & except
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)

        # count how many tasks based on each Category
        ## change to list by {}
        count_Category = Counter(task['category'] for task in tasks['tasks'])

        # task distrubution visualized by logger for simplier traceback
        logger = logging.getLogger(__name__)  # Get logger for this module
        for category, count in count_Category.items():
            logger.info("{category} count:  {count}")

        return count_Category

    except FileNotFoundError:
        logger.error("Your file {TASK_FILE} was not found!")
        # default None in return

####################

#def calculate_average_completion_time(tasks):
    '''
    Return average of day to finish the date, calculate by taking all task 
    mat trung binh bao nhieu ngay de hoan thanh cac tasks (label 'completed': True)
    tra ra 1 ket qua
    '''
logging.basicConfig(level = logging.INFO)

def calculate_average_completion_time(tasks):
    # Handling Error when open a file with try & except
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)

        for task in tasks['tasks']:
            if task.get('completed', True):
                try:
                    # we need tasks all compeled
                    completed_tasks = sum(task['completed'])

                    # convert to seconds being more appropriate to calculate
                    total_add_date = timedelta(task['add_date']).total_seconds()
                    total_finished_date = timedelta(task['finished_date']).total_seconds()

                # Traceback for any Value or Type errors when calculating NOR any tasks labeled 'completed'
                except ValueError or TypeError:
                    logging.exception('Got exception on main handler')
                    raise
            else:
                logging.info('No completed tasks found.')
                # default None in return
 
        # Difference_of_StartDate_&_EndDate
        diff_days = timedelta(total_finished_date - total_add_date).days
        # Average
        avg_cmpltd_time = diff_days / completed_tasks

        return round(avg_cmpltd_time, 2)

    except FileNotFoundError:
        logging.error("Your file {TASK_FILE} was not found!")
        # default None in return

####################

#def identify_overdue_tasks(tasks):
    '''
    Show task not finish in time
    '''
logging.basicConfig(level = logging.INFO)

def identify_overdue_tasks(tasks):
    # Handling Error when open a file with try & except
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        tasks_overdue = [] # to storing the tasks due to deadline

        for task in tasks['tasks']:
            try:

                # using formated method for date and time 
                # serve as calculations, comparisons, and manipulations
                due_date = datetime.strptime(task['due_date'], "%Y-%m-%d")
                finished_date = datetime.strptime(task['finished_date'], "%Y-%m-%d")
                if finished_date > due_date:
                    tasks_overdue.append(task.copy()) # retrieve any task without affected original data
            
            # Again, traceback for any Value or Type errors 
            except ValueError or TypeError:
                logging.exception('Got exception on main handler')
                raise
        
        if not tasks_overdue:
            logging.info("No overdue tasks found.")
            # default None in return

        return tasks_overdue
    
    except FileNotFoundError:
        logging.error("Your file {TASK_FILE} was not found!")
        # default None in return

####################

logging.basicConfig(level = logging.INFO)

def generate_productivity_report(tasks):
    '''
    Write report to a file
    '''
    # Handling Error when open a file with try & except
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)

        # Readability & Reusability
        task_completion_rate = calculate_completion_rate(tasks)
        average_completion_time = calculate_average_completion_time(tasks)
        number_overdue_tasks = identify_overdue_tasks(tasks)
        task_distribution = analyze_task_distribution(tasks)

        # data in report
        report = f"""
        Productivity Report
        -------------------
        Task Completion Rate: {task_completion_rate}%
        Average Completion Time: {average_completion_time} days
        Number of Overdue Tasks: {number_overdue_tasks}

        Task Distribution:
        {task_distribution}

            Recommendations:
            1. {"Great job on task completion!" if 100 > 80 else "Try to improve your task completion rate."}
            2. {"Work on reducing your average completion time." if 100 > 7 else "You're completing tasks in a timely manner!"}
            3. {"Focus on completing overdue tasks." if 100 else "Keep up the good work on avoiding overdue tasks!"}
                        """
        # IN CASE USING ANOTHER STR FORMAT, using to_dict data    
        #report_data = dict(report)

        # create a new file    
        with open("productivity_report.txt", "w") as f:
            f.write(report) 

            # IN CASE USING ANOTHER STR FORMAT
            # change from "f.write(report)"" to "f.write(report_data)""
            #json.dump(report_data, f, ensure_ascii = False) # dump all to the new file based on dict type data
            
    except FileNotFoundError:
        logging.error("Your file {TASK_FILE} was not found!")
        # default None in return
    

def plot_task_distribution(tasks):
    distribution = analyze_task_distribution(tasks)
    plt.figure(figsize=(10, 6))
    plt.bar(distribution.keys(), distribution.values())
    plt.title("Task Distribution")
    plt.xlabel("Task Categories")
    plt.ylabel("Number of Tasks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("task_distribution.png")
    print("Task distribution plot saved as 'task_distribution.png'")

def productivity_tracker_main(tasks):
    while True:
        print("\nProductivity Tracker")
        print("1. Generate Productivity Report")
        print("2. Plot Task Distribution")
        print("3. Return to Task Management System")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            generate_productivity_report(tasks)
        elif choice == "2":
            plot_task_distribution(tasks)
        elif choice == "3":
            print("Returning to Task Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("This module is designed to be run from the Task Management System.")
    print("Please run main.py instead.")
