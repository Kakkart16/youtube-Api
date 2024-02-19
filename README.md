# youtube-Api

# How to set up project.

1. Clone Github Repository.
2. Create a python virtual environment.
    python -m venv env
    Activate it:
    env/Scripts/activate
3. Install all the libraries
    pip install -r requirements.txt
4. Make all the migrations.
    python manage.py makemigrations
    python manage.py migrate
5. Run the python server
    python manage.py runserver