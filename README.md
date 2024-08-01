# Django Project

## Overview

This project is a Django application designed to manage user profiles and provide dashboards for doctors and patients. The application allows users to sign up, log in, and view their profile information.

## Features

- User registration and authentication
- Doctor and patient dashboards
- Profile picture upload
- Address management

## Requirements

- Python 3.9 or later
- MySQL 8.0 or later

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/guru654321/task.git
    cd banao
    ```

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**
   myenv\Scripts\activate
4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Database Settings:**
    Update the `DATABASES` settings in `project_name/settings.py` to use MySQL.

6. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```



## Acknowledgements

- Django Framework
- MySQL
- Gunicorn
