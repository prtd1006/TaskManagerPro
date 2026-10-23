# Task Manager Pro

A simple task management web application built using Python, Flask, SQLite, HTML, and CSS.

## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Store tasks in an SQLite database
- Responsive web interface

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2

## Project Structure

```text
task-manager-pro/
├── app.py
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone this repository:

   ```bash
   git clone git@github.com:prtd1006/TaskManagerPro.git
   ```

2. Open the project directory:

   ```bash
   cd task-manager-pro
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open the local address shown in your terminal, usually `http://127.0.0.1:5000`.

The SQLite database and tasks table are initialized by the application.

## Learning Outcomes

This project demonstrates practical experience with Flask routing, HTML forms, Jinja2 templates, SQLite CRUD operations, and basic input validation.
