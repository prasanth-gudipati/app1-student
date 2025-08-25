# Student Management Web Application

This project is a simple web-based Student Management System built with Flask and MongoDB, containerized using Docker. It allows users to add, view, and delete student records through a web interface.

## Features

- Add new students with details (first name, middle name, last name, DOB, address, sex)
- View all students in a table
- Delete students by ID or by name
- Simple web UI using Flask templates
- Data stored in MongoDB
- Dockerized for easy setup

## Project Structure

```
app1-student/
├── docker-compose.yml         # Multi-container setup for app, MongoDB, and Mongo Express
├── app/
│   ├── app.py                # Main Flask application
│   ├── db.py                 # MongoDB connection setup
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Docker image for Flask app
│   └── templates/            # HTML templates
│       ├── index.html
│       ├── show_students.html
│       ├── add_student.html
│       └── delete_student.html
```

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

### Setup & Run

1. Clone the repository:
	```bash
	git clone <repo-url>
	cd app1-student
	```
2. Start the application using Docker Compose:
	```bash
	docker-compose up --build
	```
3. Access the web app at [http://localhost:5000](http://localhost:5000)
4. (Optional) Access Mongo Express at [http://localhost:8081](http://localhost:8081) for DB admin

## Application Overview

- **Home Page** (`/`): Links to view, add, or delete students.
- **Show Students** (`/students`): Displays all students in a table.
- **Add Student** (`/add`): Form to add a new student.
- **Delete Student** (`/delete`): Form to delete a student by ID or name.

## API/Routes

| Route         | Methods | Description                      |
|-------------- |-------- |----------------------------------|
| `/`           | GET     | Home page                        |
| `/students`   | GET     | Show all students                |
| `/add`        | GET/POST| Add a new student                |
| `/delete`     | GET/POST| Delete a student by ID or name   |

## Database

- Uses MongoDB (default port 27017, service name `mongo` in Docker Compose)
- Collection: `students` in database `student_db`

## Dependencies

See `app/requirements.txt`:

- Flask==2.3.2
- pymongo==4.6.1

## Docker

- The Flask app is containerized (see `app/Dockerfile`).
- MongoDB and Mongo Express are included in `docker-compose.yml` for local development.

## License

MIT License (add your own license if needed)