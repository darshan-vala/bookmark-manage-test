# Demo Task - Full Stack Developer

This is a simple Django web application with a PostgreSQL database, built for the Social Booster Media demo task.

**Live Application Link:** `https://darshan-project-app.onrender.com/`

-----

## Features

1.  **CRUD API:** A full CRUD API for managing "Bookmarks" (`/api/bookmarks/`).
2.  **3rd Party API:** An endpoint that fetches data from an external API (`/api/external-users/`).
3.  **Data Visualization:** A simple bar chart showing the priorities of all saved bookmarks (`/api/chart/`).

-----

## API Endpoints

  * `GET, POST /api/bookmarks/`: List all bookmarks or create a new one.
  * `GET, PUT, PATCH, DELETE /api/bookmarks/{id}/`: Read, update, or delete a specific bookmark.
  * `GET /api/external-users/`: Fetches sample user data from `jsonplaceholder`.
  * `GET /api/chart/`: Renders the HTML page with the data visualization.
  * `GET /api/chart-data/`: The internal API that provides data to the chart.

-----

## How to Run Locally

1.  Clone the repository:

    ```bash
    git clone <this-repo-url>
    cd <repo-name>
    ```

2.  Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Setup (Required):**
    This project requires a PostgreSQL database.

      * Install PostgreSQL on your local machine.
      * Create a new local database (e.g., `bookmark_db`).
      * You must set the `DATABASE_URL` environment variable to point to your local database. For example:
        ```bash
        # You can set this in your terminal before running the server
        export DATABASE_URL="postgres://YOUR_LOCAL_USER:YOUR_LOCAL_PASSWORD@localhost:5432/bookmark_db"
        ```

5.  Run migrations:

    ```bash
    python manage.py migrate
    ```

6.  Run the development server:

    ```bash
    python manage.py runserver
    ```

7.  Access the application at `http://127.0.0.1:8000/`.