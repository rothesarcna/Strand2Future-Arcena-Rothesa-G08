# Strand2Future
### Choose Your Course. Plan Your Future.

Strand2Future is a web-based course guidance system designed to help Grade 11 and Grade 12 students explore possible college courses based on their interests, skills, and preferences.

The system aims to help students make more informed decisions about their future by providing course information, career opportunities, course recommendations, and advance study topics.

## Project Overview

Choosing a college course can be difficult, especially for students who are still unsure about their interests and future career paths.

Strand2Future provides a centralized platform where students can explore different college courses, understand their possible career opportunities, and discover the subjects and skills they may encounter in college.

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
- Secure password handling
- Student profile viewing and editing
- Student dashboard
- Course catalog
- Course details and descriptions
- Course curriculum and subject information
- Career opportunities and related skills
- Course search

### Admin Features

- Administrator login
- Admin dashboard
- Access to Django Administration
- Management of registered users and system records through Django Admin

### Features Under Development

- Interest and skills assessment
- Ranked course recommendations
- Saved courses
- Assessment history
- Advance Study Guide
- Additional course exploration features

*The system is being developed incrementally. Some features have database models prepared but are not yet fully implemented in the user interface.*

## Design

Strand2Future uses a clean and modern interface designed to make course exploration simple and accessible.

Design elements include:

- Green and white color scheme
- Sidebar navigation
- Dashboard summary cards
- Rounded content cards
- Responsive page layouts
- Consistent typography and spacing
- Plus Jakarta Sans font

## Project Structure

```text
Strand2Future-Arcena-Rothesa-G08/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── assessments/
│   ├── migrations/
│   ├── models.py
│   └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── courses/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── recommendations/
│   ├── migrations/
│   ├── models.py
│   └── admin.py
│
├── studyguide/
│   ├── migrations/
│   ├── models.py
│   └── admin.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── accounts/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   └── edit_profile.html
│   │
│   ├── core/
│   │   ├── home.html
│   │   ├── dashboard.html
│   │   └── admin_dashboard.html
│   │
│   ├── courses/
│   │   ├── course_list.html
│   │   └── course_detail.html
│   │
│   └── base.html
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

*Note: The structure above shows the main project files. Some folders may contain additional files and configurations.*

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

Install the required packages using the provided requirements file:

```bash
pip install -r requirements.txt
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

**Important:** The `.env` file is excluded from Git through `.gitignore`. Do not upload it or share your database credentials publicly.

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
| Student Login | http://127.0.0.1:8000/accounts/login/ |
| Student Registration | http://127.0.0.1:8000/accounts/register/ |
| Student Dashboard | http://127.0.0.1:8000/dashboard/ |
| Student Profile | http://127.0.0.1:8000/accounts/profile/ |
| Course Catalog | http://127.0.0.1:8000/courses/ |
| Admin Dashboard | http://127.0.0.1:8000/admin-dashboard/ |
| Django Administration | http://127.0.0.1:8000/admin/ |

## Version Control

The project uses Git and GitHub for source code management.

- **main:** Main project branch.
- **develop:** Development branch for ongoing changes.

Development changes are pushed to the `develop` branch and merged into `main` when ready.

## Project Repository

GitHub: https://github.com/rothesarcna/Strand2Future-Arcena-Rothesa-G08

## Project Status

Strand2Future is currently under development.

The initial development includes the PostgreSQL database connection, student authentication, profile management, role-based dashboards, and course catalog interface.

The remaining features, including assessments, course recommendations, saved courses, assessment history, and the Advance Study Guide, are planned for subsequent development.

---

**Strand2Future**

*Choose Your Course. Plan Your Future.*
