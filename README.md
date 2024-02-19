# youtube-Api

# How to set up project.

1.  Clone Github Repository.
2.  Create a python virtual environment.
    ```
        python -m venv env
3.  Activate virtual env:
    ```
        env/Scripts/activate
4.  Install all the libraries
    ```
        pip install -r requirements.txt
5.  Make all the migrations.
    ```
        python manage.py makemigrations
        python manage.py migrate
6.  Create super user
    ```
        python manage.py createsuperuser
6. Run the python server
    ```
        python manage.py runserver
7. Run Celery worker and beat
    ```
        celery -A core worker -l info
        celery -A core beat -l info

# API Endpoints

1.  Dashboard
    ```
    http://127.0.0.1:8000/dashboard/

2.  Admin Panel
    ```
    http://127.0.0.1:8000/admin/

3.  ```
    http://127.0.0.1:8000/videos/