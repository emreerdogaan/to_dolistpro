# ToDo List Pro

A simple, clean, and responsive ToDo application designed to manage daily tasks. I built this project to practice full-stack web development, focusing on building clean RESTful APIs with Django and designing a modern, interactive frontend without relying on heavy frameworks.

The app features an elegant dark-theme dashboard with a glassmorphic UI, dynamic task filters (by category and priority), search capability, and a real-time progress tracker.

## Features
- **Dynamic Dashboard**: A fully responsive interface with glassmorphic cards, smooth hover effects, and micro-animations.
- **RESTful API Backend**: Written in Django, handling standard GET, POST, PUT/PATCH, and DELETE requests for all tasks.
- **Task Sorting & Filtering**: Filter tasks instantly by status (Pending, Completed), Category (Work, Personal, Shopping, Health, Other), or Priority (High, Medium, Low).
- **Search Functionality**: Quickly find tasks by typing in the search bar.
- **Progress Tracker**: A circular progress bar that updates dynamically as tasks are checked off.
- **Vanilla Frontend**: Built entirely with pure CSS3 and JavaScript (Fetch API) for fast, reload-free interactions.

## Tech Stack
- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite3
- **Icons**: FontAwesome

## Setup and Installation

### Prerequisites
- Python installed on your system.

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/emreerdogaan/to_dolistpro.git
   cd to_dolistpro
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Open the App**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.
