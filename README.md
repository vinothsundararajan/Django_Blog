# Django:
    requirments:
    	pip
    	virtualenv
    	python3
# install django on virtual env:
    	#python -m virtualenv djanho_venv
    		~ run activate.bat from scripts 
    	 (ADMIN)
    	OR THAT PLAN AND EXECUTE	 Set-ExecutionPolicy Unrestricted -Force
    	#C:\Vinoth\Python\django_project\django_venv\Scripts>activate.bat
    	activate.bat

# Upgrade PIP

    (django_venv) C:\Vinoth\Python\django_project\django_venv\Scripts>python -m pip install --upgrade pip
    python -m pip install --upgrade pip
    Collecting pip
      Downloading pip-20.1-py2.py3-none-any.whl (1.5 MB)
    Installing collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 20.0.2
        Uninstalling pip-20.0.2:
          Successfully uninstalled pip-20.0.2
    Successfully installed pip-20.1
    
# Add Django~=2.2.4 to the requirements.txt
    drwxr-xr-x 1 Vinoth Sundararajan 1049089  0 Apr 30 12:00 django_venv
    -rw-r--r-- 1 Vinoth Sundararajan 1049089 13 Apr 30 12:01 requirements.txt

# Project: (BLOG)
    	django-admin startproject blog
    		to start server go to blog directory
    			python manage.py runserver (127.0.0.0:8000)
    		to stop cltl +c
# App:	
    delete the migrations folder in app and then do :
    python manage.py makemigrations
    python manage.py migrate
    python manage.py migrate --run-syncdb
