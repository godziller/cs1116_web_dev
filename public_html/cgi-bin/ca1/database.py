import os 
import sqlite3

DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'todo.db')

db = ""

def get_db():
    db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    return db

def close_db(db, e=None):
    db.close()

def get_all_tasks(user_id): #TODO:
    """ Get all task for a user
    
    Arguements:
    user_id -- the unique id for a user - aka PK in user database

    Returns:
    task_list -- list of tasks, where tasks is a dict of its variables.
    """

    return


def get_tasks_by_project(user_id, project_id): #TODO:
    """ Get user's tasks filtered by project id.

    Arguements:
    user_id     -- the unique id for a user - aka PK in the user database.
    project_id   -- the unique id for a user's project - aka PK in project db

    Returns:
    task_list -- list of tasks, where tasks is a dict of its variables.
    """
    
    return

def create_task(user_id, task): # TODO:
    """ Create a new task in the task database
    
    Arguements:
    user_id -- unique identifier for the user creating task
    task -- dict containing task values

    Returns:
    task_id -- unique identifier for the created task
    """
    return
