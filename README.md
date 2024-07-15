# Swift-Dynamics-Test

# School Management System

The School Management System is a Django application that facilitates management of schools, classrooms, teachers, and students.

## Features

- **School Management**
  - Create, read, update, delete (CRUD) operations for schools.
  - Filter schools by name.

- **Classroom Management**
  - Create, read, update, delete (CRUD) operations for classrooms.
  - Filter classrooms by associated school.

- **Teacher Management**
  - Create, read, update, delete (CRUD) operations for teachers.
  - Filter teachers by school, classroom, first name, last name, and gender.

- **Student Management**
  - Create, read, update, delete (CRUD) operations for students.
  - Filter students by school, classroom, first name, last name, and gender.

- **API Endpoints**
  - Comprehensive RESTful APIs for managing schools, classrooms, teachers, and students.

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/nutthapong-patchotchai/Swift-Dynamics-Test.git
   cd Swift-Dynamics-Test/5_rest_api/
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```
   python manage.py migrate
   ```

4. **Run the development server:**
   ```
   python manage.py runserver
   ```

5. **Access the API at http://localhost:8000/**

## Usage

### API Endpoints

#### Schools

- **GET `/api/schools/`**: Retrieve all schools.
- **POST `/api/schools/`**: Create a new school.
- **GET `/api/schools/{id}/`**: Retrieve details of a school.
- **PUT `/api/schools/{id}/`**: Update a school.
- **DELETE `/api/schools/{id}/`**: Delete a school.

#### Classrooms

- **GET `/api/classrooms/`**: Retrieve all classrooms.
- **POST `/api/classrooms/`**: Create a new classroom.
- **GET `/api/classrooms/{id}/`**: Retrieve details of a classroom.
- **PUT `/api/classrooms/{id}/`**: Update a classroom.
- **DELETE `/api/classrooms/{id}/`**: Delete a classroom.

#### Teachers

- **GET `/api/teachers/`**: Retrieve all teachers.
- **POST `/api/teachers/`**: Create a new teacher.
- **GET `/api/teachers/{id}/`**: Retrieve details of a teacher.
- **PUT `/api/teachers/{id}/`**: Update a teacher.
- **DELETE `/api/teachers/{id}/`**: Delete a teacher.

#### Students

- **GET `/api/students/`**: Retrieve all students.
- **POST `/api/students/`**: Create a new student.
- **GET `/api/students/{id}/`**: Retrieve details of a student.
- **PUT `/api/students/{id}/`**: Update a student.
- **DELETE `/api/students/{id}/`**: Delete a student.

### Additional Information

- Customize models and serializer configurations to suit project requirements.
- Utilize Django Filters for flexible data filtering in APIs.

## Requirements

- Python 3.10+
- Django 5.0.4
- Django REST Framework 3.15.1
- django-filter 24.2