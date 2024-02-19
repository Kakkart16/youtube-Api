# youtube-Api

# How to set up project.

1. Clone Github Repository.
2. Create a python virtual environment.
    ```
        python -m venv env
3. Activate virtual env:
    ```
        env/Scripts/activate
4. Install all the libraries
    ```
        pip install -r requirements.txt
5. Make all the migrations.
    ```
        python manage.py makemigrations
        python manage.py migrate
6. Run the python server
   ```
    python manage.py runserver