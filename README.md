# Event Management System
 
**Description**

The Event Management System is a Python-based application developed using Object-Oriented Programming (OOP) principles and SQLite for database management. The project is designed to simplify the process of organizing and managing events through a modular and scalable architecture. Each module is responsible for a specific functionality, making the application easy to understand, maintain, and extend.

The system provides functionalities for user management, institution management, event creation, participant registrati ons, approval workflows, notifications, dashboard reporting, and data export. The project is currently developed in pure Python and is structured to allow seamless integration with the Django framework in the future.

**Features**

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
- Modular Architecture
- Object-Oriented Programming (OOP)

**Project Structure**

```text
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
```

**Technologies Used**

- Python 3
- SQLite3
- OpenPyXL
- Matplotlib
- Django
- PYTHON SMTP

**Installation**

Clone the repository:

```bash
git clone https://github.com/Tanishk-a/event-management-system-python.git
```

Navigate to the project directory:

```bash
cd event-management-system-python
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Application

```bash
python main.py
```

Database

The application uses SQLite for data storage./actual versions will have postgress

Database File

```text
event_management.db
```

**Project Modules**

- Accounts
- Institutions
- Events
- Registrations
- Approvals
- Notifications
- Dashboard
- Calendar View
- Exports
- Database
- Common Utilities

**Future Enhancements**

- Django Backend Integration
- REST API Development
- Email Notifications
- Interactive Dashboard
- Calendar Integration
- PDF Report Generation
- Advanced Search and Filtering
- Responsive Web Interface

