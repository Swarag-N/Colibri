# Colibri



## Get Started
1. Clone the repo 
2. Create a virtual env
    ```
    python3 -m venv venv
    source ./venv/bin/activate 
    ```
3. Install Dependeince
    - pip
    ```
    pip install -r requirements.txt
    ```
4. Make Migrations
    - shell
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Create Super User
    - shell
    ```shell
    python manage.py createsuperuser
    ```
5. Start Server
    - Django Server
    ```
    python manage.py runserver


## ToDo
- JWT for auth (Could you simple-JWT)
