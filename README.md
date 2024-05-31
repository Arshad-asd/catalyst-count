# Catalyst-Count App

Welcome to our Django-based web application! This project is designed to streamline data handling tasks, including the efficient uploading of large files, user management, and dynamic query building. With a focus on usability and performance, this application leverages Django's robust features alongside modern front-end technologies to provide a seamless and responsive user experience.

## Core Features

- User Management: Easily manage users within the application. Add new users, view user lists, and remove users as needed, all from a user-friendly interface.
- Large File Uploads: Utilize chunked uploading to handle large files (up to 1GB or more) efficiently. The application provides real-time progress feedback to ensure a smooth upload experience.
- Query Builder: Construct complex queries with ease using a flexible query builder form. Input fields include keyword, industry, year founded, city, state, country, and employee range, allowing for precise data querying.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Arshad-asd/catalyst-count.git
```

2. Create and activate a virtual environment:

```bash
python -m venv env
```

```bash
# On Windows: .\env\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```

```bash
cd catalyst_count
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the development server:

```bash
python manage.py runserver
```

6. Access the API at [http://localhost:8000/api/](http://localhost:8000/)

## URL Endpoints


### URL Endpoints

#### 1. User Management:

- `GET /accounts/login/`: Log in an existing user.
- `GET /accounts/signup/`: Register a new user.
- `GET /user_list/`: List all users.
- `POST /remove_user/<int:user_id>/`: Remove a specific user by ID.

#### 2. File Upload:

- `GET /upload_data/`: Display the upload data form.
- `POST /upload_chunk/`: Handle chunked file uploads.

#### 3. Query Builder:

- `GET /query_builder/`: Display the query builder form.

#### 4. General:

- `GET /`: Display the welcome page.
