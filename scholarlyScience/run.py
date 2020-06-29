import os

os.system("virtualenv -p python3 venv")
os.system("source venv/bin/activate")
os.system("pip install -r requirements.txt")
os.system("python3 manage.py makemigrations")
os.system("python3 manage.py migrate")
os.system("python3 manage.py runserver")
