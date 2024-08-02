Django Project
Overview
This project is a Django application designed to manage user profiles and provide dashboards for doctors and patients. The application allows users to sign up, log in, and view their profile information.

Features
User registration and authentication
Doctor and patient dashboards
Profile picture upload
Address management
Requirements
Python 3.9 or later
MySQL 8.0 or later
Installation
Clone the Repository:

git clone https://github.com/guru654321/task.git
cd banao
Create a Virtual Environment:

python -m venv venv
Activate the Virtual Environment: myenv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt
Configure Database Settings: Update the DATABASES settings in project_name/settings.py to use MySQL.

Run Migrations:

python manage.py migrate
Run the Development Server:

python manage.py runserver
Acknowledgements
Django Framework
MySQL
Gunicorn
