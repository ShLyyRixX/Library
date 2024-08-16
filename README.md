### -----INSTALLATION AND SETUP-----

 1. Clone the repository

    ```bash

    git clone https://github.com/ShLyyRixX/Library.git
    cd library
    ```

 2. Create a PostgreSQL database.
    Make sure you have PostgreSQL installed. Run the following commands to create a new database:

    ```sql

    CREATE DATABASE library;
    CREATE USER library WITH PASSWORD 'library';
    ALTER ROLE library SET client_encoding TO 'utf8';
    ALTER ROLE library SET default_transaction_isolation TO 'read committed';
    ALTER ROLE library SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE library TO library;
    ```

3. Install dependencies.
    Create a virtual environment and activate it:

    ```bash

    python -m venv venv
    venv\Scripts\activate
    ```

    Then install the required packages:

    ```bash

    pip install -r requirements.txt
    ```

4. Apply migrations.
    Run the migrations to set up the database schema:

    ```bash

    python manage.py migrate
    ```

5. Run the server.
    Start the Django development server:

    ```bash

    python manage.py runserver
    ```

The API will be available at "http://127.0.0.1:8000/api/books/".

### -----HOW TO USE-----

To use the functions to create a book and get a filtered list of books by author, publication date, or language, USE BUILT-IN DJANGO REST FRAMEWORK INTERFACE IN BROWSER.

Use the address “http://127.0.0.1:8000/api/books/BOOK_ID/” to use the detailed book information features. 
Beforehand, replace “BOOK_ID” in the address with the existing ID of the book you have already added using POST request.

Pagination will automatically appear when you add more than 10 books.

### -----RUNNING TESTS-----

To run the unit tests, use the following command:


    python manage.py test
    

