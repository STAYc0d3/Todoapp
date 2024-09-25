# todoapp – Django Task Management Application

## Description:
**todoapp** is a task management application built using Django, allowing users to create, edit, and manage tasks efficiently.

## Features:
- Task creation and editing.
- User authentication and task assignment.
- Responsive design using Bootstrap.
- Validation and handling of task forms.
- SQLite as the database for task storage.

## Technologies Used:
- **Django** – Main backend framework.
- **HTML/CSS** – For UI design and structure.
- **Django Forms** – For task creation and modification.
- **SQLite** – For task data storage.
- **Django Templating System** – For dynamic content rendering.
- **Bootstrap** – For responsive design.
- **ChatGPT Assistance** – Generated HTML and CSS for faster development.

## How to Run Locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todoapp.git
    cd todoapp
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # For Linux/macOS
    venv\Scripts\activate      # For Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open the app in your browser at `http://127.0.0.1:8000/`.

## Screenshots:
![Task List](screenshots/task_list.png)
![Create Task](screenshots/create_task.png)

## Future Improvements:
- Adding task categorization and filtering.
- Integration with external APIs for better task management.
