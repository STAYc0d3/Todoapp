# Todoapp – Django Task Management Application

## Introduction:
This is my first pet project that I'm publishing on GitHub. **Todoapp** is a task management application built using Django, allowing users to create, edit, and manage tasks efficiently. This project demonstrates my understanding of web development technologies and my ability to integrate various tools and frameworks.

## Features:
- Task creation, editing, and deletion.
- Validation and handling of task forms.
- SQLite as the database for task storage.

## Technologies Used:
- **Django**: Used for backend logic, request handling, and database management.
- **HTML/CSS**: For designing and structuring the user interface.
- **Django Forms**: Implemented to handle task creation and modification with built-in validation.
- **SQLite**: As a lightweight database for managing task records.
- **Django Templating System**: For rendering dynamic content and building user-friendly views.
- **Git and GitHub**: For version control and project collaboration.
- **ChatGPT Assistance**: Used for generating parts of the HTML, CSS, and troubleshooting issues, significantly speeding up development.

## Installation

To run this project locally, follow these steps:

### Step 1: Clone the repository
```
git clone https://github.com/STAYc0d3/Todoapp.git
cd Todoapp
```
### Step 2: Create a virtual environment
Create a virtual environment and activate it:

On Linux/macOS:
```
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```
python -m venv venv
venv\Scripts\activate
```
### Step 3: Install the required packages
Install all the dependencies listed in the requirements.txt file:
```
pip install -r requirements.txt
```
### Step 4: Apply migrations
Set up the database by applying migrations:
```
python manage.py migrate
```
### Step 5: Create a superuser
Create a superuser for admin access:
```
python manage.py createsuperuser
```
### Step 6: Run the development server
Run the Django development server to test the application locally:
```
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

## Adding a Task
- Log in with your credentials or create a new user.
- Add a new task by navigating to the task creation page.
- Fill in the task details and submit the form.
- Edit or delete tasks via the task list page.
## Admin Access
You can manage tasks, users, and other parts of the application via the Django admin panel. Access it by navigating to /admin/ and logging in with your superuser credentials.
## Screenshots
- Task creation form ![image](https://github.com/user-attachments/assets/d47e2a56-2f9e-49e7-bc92-8d2cc0711bba)
- Task list ![image](https://github.com/user-attachments/assets/1c9be02f-dcd1-4581-9cfc-5257a1fcbdd9)

