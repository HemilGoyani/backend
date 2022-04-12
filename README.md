# backend

# setup project and run


1. Clone the project from git repository and move into the project directory.

    ```sh
    git clone https://github.com/HemilGoyani/backend.git
    cd backend/
    ```
   
2. Create virtual environment and activate the environment.

    ```sh
    1.virtualenv env
    2.source env/bin/activate

    ```

3. install the requirement.txt file

    ```sh
    pip install -r requirements.txt

    ```

4. Migrate the database

    ``` sh
    python manage.py migrate
    
    ```
5. Run the project
    ```sh
    python manage.py runserver 0.0.0.0:8000

    ```
