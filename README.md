# Strand2Future
### Choose Your Course. Plan Your Future.

Strand2Future is a web-based course guidance system designed to help Grade 11 and Grade 12 students explore possible college courses based on their interests and skills.

The system aims to help students make more informed decisions about their future by providing course recommendations, course information, career opportunities, and advance study topics.

## Project Overview

Choosing a college course can be difficult, especially for students who are still unsure about their interests and future career paths.

Strand2Future provides a centralized platform where students can explore different courses, learn about their possible career opportunities, and discover subjects and topics they may encounter in college.

## Technologies Used

- **Backend:** Python and Django
- **Frontend:** HTML, CSS, and JavaScript
- **Database:** PostgreSQL through Supabase
- **Typography:** Plus Jakarta Sans
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## Main Features

### Student Features

- Student registration and login
- Student profile information
- Course catalog and course details
- Course curriculum and subject information
- Career opportunities and related skills
- Interest and skills assessment
- Ranked course recommendations
- Saved courses
- Assessment history
- Advance Study Guide

### Admin Features

- Manage student accounts
- Manage course information
- Manage subjects and curricula
- Manage careers and skills
- Manage assessment questions and choices
- Manage course scoring rules
- Manage Advance Study Guide topics

*Some features are still under development.*

## Design

Strand2Future uses a clean and modern interface with:

- Green and white color scheme
- Sidebar navigation
- Dashboard summary cards
- Rounded content cards
- Responsive page layouts
- Consistent typography and spacing

## Project Structure

```text
Strand2Future-Arcena-Rothesa-G08/
│
├── accounts/
├── assessments/
├── config/
├── core/
├── courses/
├── recommendations/
├── studyguide/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── accounts/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── core/
│   │   ├── home.html
│   │   └── dashboard.html
│   │
│   ├── courses/
│   │   ├── course_list.html
│   │   └── course_detail.html
│   │
│   └── base.html
│
├── .env
├── .gitignore
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rothesarcna/Strand2Future-Arcena-Rothesa-G08.git
```

### 2. Open the Project Folder

```bash
cd Strand2Future-Arcena-Rothesa-G08
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

### 4. Install Dependencies

```bash
pip install django psycopg[binary] python-dotenv
```

### 5. Configure Environment Variables

Create a `.env` file in the same directory as `manage.py`.

Add the following variables:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=postgres
DB_USER=your_supabase_database_user
DB_PASSWORD=your_supabase_database_password
DB_HOST=your_supabase_database_host
DB_PORT=5432
```

Replace the example values with your actual Django and Supabase credentials.

**Important:** Do not upload your `.env` file or share your database credentials publicly.

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your administrator account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

**http://127.0.0.1:8000/**

## Accessing the System

| Page | URL |
|---|---|
| Home | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Registration | http://127.0.0.1:8000/accounts/register/ |
| Student Dashboard | http://127.0.0.1:8000/dashboard/ |
| Course Catalog | http://127.0.0.1:8000/courses/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

## Project Repository

GitHub: https://github.com/rothesarcna/Strand2Future-Arcena-Rothesa-G08

## Project Status

Strand2Future is currently under development. The project is being developed incrementally, with its database structure, student authentication, course catalog, and dashboard interface being established before the remaining features are completed.

---

**Strand2Future**

*Choose Your Course. Plan Your Future.*
