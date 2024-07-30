import os
import json
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

#####################

#def add_task(tasks):
    '''
    Show all task
    task = {
        "id": 
        "title": 
        "category": 
        "description":
        "add_date"
        "due_date": 
        "finished_date": 
        "completed": 
    }
    '''
# Making a sketch-liked for multiple inputs by Encoding
class Adding:
    def __init__(self, 
                 id, title, category, description, add_date, due_date, finished_date, completed):
        self.id = id
        self.title = title
        self.category = category
        self.description = description
        self.add_date = add_date
        self.due_date = due_date
        self.finished_date = finished_date
        self.completed = completed

# Encoding function    
def encode_A(obj):
     if isinstance(obj, Adding):
         return {'id': obj.id, 
                 'title': obj.title,
                 'category': obj.category,
                 'description': obj.description,
                 'add_date': obj.add_date,
                 'due_date': obj.due_date,
                 'finished_date': obj.finished_date,
                 'completed': obj.completed}
     return obj

# test an input our (your new object will be inputted)
Task_2 = Adding(2, 'Failed Python project', 
                    'Studying', 
                    'Failed any tasks', 
                    '2024-07-15', 
                    '2024-07-30', 
                    '2024-07-29', 
                    False
                        )

# open Json file with the Adding
def add_task(tasks):
    with open(TASKS_FILE , 'w') as file:
        json.dump(Task_2, file, default = encode_A)

################

#def list_tasks(tasks):
    '''
    Show all task
    '''
# retrieve the Json file after made our inputs
def list_tasks(tasks):
    with open(TASKS_FILE , 'r') as file:
        return json.load(file)

################

#def mark_task_completed(tasks):
    '''
    Change state of the task to complete and add finish date
    '''
import datetime

def mark_task_completed(tasks):
    # your ID depends on how many IDs would be inputted?
    # Firstly, It's None
    task_id = None
    
    while task_id is None:
        try: 
            # Then, try to input your existing ID
            task_id = int(input('Enter the ID of the task to mark as completed: '))
            # more user-friendly if IDs not been inputted
            if task_id == 'q':
                break
        except ValueError:
            print(f"Task ID {task_id} hasn't been inputted. You can enter q to quit")
    
    # while 'task' is a single Dictionary contains a List of objects, 
    # and   'tasks' likely holds a list of many Dictionaries
    for task in tasks:
        if task['id'] == task_id:
            # change the status & update the finished date
            task['completed'] = True
            task['finished_date'] = datetime.datetime.now().strftime('%Y-%m-%d') 
            print(f'Task ID {task_id} marked as completed.')
            break
    
    # Make sure the IDs must be existing
    else:
    # if task_id is not None and task_id != 'q':
        print(f'Task ID {task_id} still not found.')
    
################

#def delete_task(tasks):
    '''
    Delete a task
    '''

def delete_task(tasks):
    # your ID depends on how many IDs would be inputted?
    # Firstly, It's None
    task_id = None
    
    while task_id is None:
        try: 
            # Then, try to input your existing ID
            task_id = int(input("Enter the ID of the task to delete: "))
        # more user-friendly if IDs not been inputted
            if task_id == 'q':
                break
        except ValueError:
            print(f"Task ID {task_id} hasn't been inputted. You can enter q to quit")

    # while 'task' is a single Dictionary contains a List of objects, 
    # and   'tasks' likely holds a list of many Dictionaries
    for index, task in tasks:
        if task['id'] == task_id:
            # delete the needed ID
            del tasks[index]
            print(f'Task ID {task_id} deleted successfully')
            break

    # Make sure the IDs must be existing
    else:
    # if task_id is not None and task_id != 'q':
        print(f'Task ID {task_id} still not found.')

################

#def search_tasks(tasks):
    '''
    Find task by keyword, check the keyword is inside description, title or id 
    '''

def search_tasks(tasks, keyword):
    # your keywords should be to search?
    # Firstly, It's None
    keyword = None
    
    while keyword is None:
        try: 
            # Then, try to input your existing ID
            keyword = input('Enter a keyword to search for: ').lower()
            # more user-friendly if there are not any keywords
            if keyword == 'q':
                break
        except ValueError:
            print(f'There are not any {keyword} matching with your need!? You can enter q to quit')
    
    # First, draft a none task & a list of none detail
    tasks_to_find = []
    task_details = '' # to storing the keywords within

    # any keyword have to satisfy in the any needs (3)
    for task in tasks:
        if any( keyword in field.lower() for field in [task['id'], task['title'], task['description']] ):
            tasks_to_find.append(task) # add the entire task (dictionary) as a new element that meet our keyword
            # accumulate details in a string
            task_details += f"- ID: {task['id']}\n"
            task_details += f"- Title: {task['title']}\n"
            task_details += f"  Description: {task['description']}\n"

    # If no tasks required
    if not tasks_to_find:
        print(f"No tasks found matching with your '{keyword}' keyword.")
    # More readability
    else:
        # We counts how many tasks contains the desired keyword
        print(f"Found {len(tasks_to_find)} tasks matching the '{keyword}' as the keyword.")
        print(task_details)
    
    return {'search results': task_details,
            'matching_tasks': tasks_to_find}
