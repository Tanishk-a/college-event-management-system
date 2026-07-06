## Event Management System

Description

The Event Management System is a Python-based application developed using Object-Oriented Programming (OOP) principles and SQLite for database management. The project provides a structured solution for managing events within an institution or organization. It follows a modular architecture where each module is responsible for a specific functionality, making the project organized, maintainable, and scalable.

The application includes modules for user management, institution management, event management, registrations, approvals, notifications, dashboards, and report generation. The business logic is separated from data models to improve code organization and simplify future development. The project is being developed in pure Python and is structured for easy integration with the Django framework in future phases.

Features

- User Registration and Authentication
- Role-Based Access Control
- Institution Management
- Event Creation and Management
- Event Registration
- Multi-Level Approval Workflow
- Notification System
- Dashboard and Reports
- Excel Report Export
- SQLite Database Integration
- Modular Project Structure

Project Structure


project_root/
│
├── manage.py
├── requirements.txt
├── .env
│
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py          # User, StudentProfile, StaffProfile
│   ├── views.py           # Login, Logout, Profile
│   ├── services.py        # Business Logic
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── permissions.py
│   ├── signals.py
│   └── apps.py
│
├── institutions/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
│
├── events/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── permissions.py
│   ├── validators.py
│   └── signals.py
│
├── registrations/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── approvals/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── notifications/
│   ├── models.py
│   ├── email.py
│   ├── services.py
│   ├── signals.py
│   ├── apps.py
│   └── admin.py
│
├── exports/
│   ├── views.py
│   ├── services.py
│   ├── utils.py
│   └── urls.py
│
├── calendar_view/
│   ├── views.py
│   ├── services.py
│   └── urls.py
│
├── dashboard/
│   ├── views.py
│   ├── services.py
│   └── urls.py
│
└── common/
    ├── constants.py
    ├── decorators.py
    ├── helpers.py
    ├── validators.py
    ├── permissions.py
    └── exceptions.py


Technologies Used

- Python 3
- SQLite3
- Object-Oriented Programming (OOP)
- OpenPyXL
- Matplotlib

Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

Running the Project

```bash
python main.py
```

Database

The application uses SQLite for data storage.

Database File

```text
event_management.db
```

Development Phases

Phase 1
- Project Setup
- Database Configuration
- Common Utilities

Phase 2
- Accounts Module

Phase 3
- Institution Module

Phase 4
- Events Module

Phase 5
- Registrations Module

Phase 6
- Approvals Module

Phase 7
- Notifications Module

Phase 8
- Dashboard Module

Phase 9
- Export Module

Phase 10
- Django Integration

Future Enhancements

- Django Web Application
- REST API Development
- Email Notifications
- Interactive Dashboard
- Calendar Integration
- PDF Report Generation
- Advanced Search and Filtering
- Web-Based User Interface

