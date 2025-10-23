# Demo Task - Full Stack Developer

This is a simple Django web application with a PostgreSQL database, built for the Social Booster Media demo task.

**Live Application Link:** `https://darshan-project-app.onrender.com/`

-----

## Task Requirements Met

This project fulfills the core requirements of the demo task:

1.  **CRUD Functionality:** A full REST API with Create, Read, Update, and Delete functionality is available for "Bookmarks" at the `/api/bookmarks/` endpoint.
2.  **API Integration:** The requirement "At least one API integration example" is met. The endpoint `/api/external-users/` pulls live data from the public `jsonplaceholder` third-party API.
3.  **Data Visualization:** A simple data visualization feature is available at `/api/chart/`, which renders a bar chart of bookmark priorities retrieved from the database.

-----

## API Endpoints

  * `GET, POST /api/bookmarks/`: List all bookmarks or create a new one.
  * `GET, PUT, PATCH, DELETE /api/bookmarks/{id}/`: Read, update, or delete a specific bookmark.
  * `GET /api/external-users/`: **(3rd-Party API Integration)** Fetches sample user data from `jsonplaceholder`.
  * `GET /api/chart/`: **(Visualization)** Renders the HTML page with the data visualization.
  * `GET /api/chart-data/`: The internal API that provides data to the chart.

-----

## How to Perform CRUD Operations

You can use any API client (like Postman, Insomnia) or `curl` to interact with the live API.

**Note:** Replace `https-live-url` with `https://darshan-project-app.onrender.com` for the live app, or `http://127.0.0.1:8000` for local testing.

### Create (POST)

Create a new bookmark.

```bash
curl -X POST \
  https-live-url/api/bookmarks/ \
  -H 'Content-Type: application/json' \
  -d '{
        "title": "Google",
        "url": "https://google.com",
        "priority": 1
    }'
```

### Read (List - GET)

Get a list of all bookmarks.

```bash
curl -X GET https-live-url/api/bookmarks/
```

### Read (Detail - GET)

Get a single bookmark by its ID (e.g., ID 1).

```bash
curl -X GET https-live-url/api/bookmarks/1/
```

### Update (PUT)

Update an existing bookmark (e.g., ID 1).

```bash
curl -X PUT \
  https-live-url/api/bookmarks/1/ \
  -H 'Content-Type: application/json' \
  -d '{
        "title": "Google Search",
        "url": "httpsS://google.com",
        "priority": 2
    }'
```

### Delete (DELETE)

Delete an existing bookmark (e.g., ID 1).

```bash
curl -X DELETE https-live-url/api/bookmarks/1/
```

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