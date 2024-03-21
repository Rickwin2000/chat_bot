import multiprocessing
import os 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Gunicorn configuration for Django

# Bind to port 8000 on localhost
bind = '127.0.0.1:8000'

# Set the number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Set the worker class
worker_class = 'gthread'

# Set the maximum number of requests a worker will process before restarting
max_requests = 1000

# Set the maximum number of simultaneous clients that a single worker can handle
worker_connections = 1000

# Set the path to your Django project directory
chdir = os.path.join(BASE_DIR)

# Specify the path to your Django WSGI application
# Replace 'your_project_name' with the actual name of your Django project
# Replace 'your_project_name.wsgi:application' with the path to your WSGI application object
# For example, if your project is named 'myproject' and the WSGI application object is named 'application',
# you would use 'myproject.wsgi:application'
pythonpath = chdir
django_settings = 'chat.settings'
app = 'chat.wsgi:application'

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'
