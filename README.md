
# Customer Management Project

This project is a customer management system built with Django and MongoDB. The system has two types of users: Makers and Checkers. Makers can upload customer data, and Checkers can approve or decline the customer data uploaded by their assigned Makers.

## Features

- Two types of users: Maker and Checker.
- Makers can upload customer data, including a photo and a resume.
- Checkers can view customer data uploaded by their assigned Makers and either approve or decline the customers.
- Customer status (Pending, Approved, Declined) management.
- Hierarchical access control: Checkers can only access data from their assigned Makers.

## Technical Specifications

- **Language**: Python
- **Framework**: Django
- **Database**: MongoDB

## Deliverables

The `deliverables/` folder contains:

1. **Database Dump**: `customer_management_db_dump.zip` - MongoDB database dump.
2. **User Credentials**: `user_credentials.txt` - User credentials for Makers and Checkers.
3. **Hierarchy Diagram**: `hierarchy_diagram.png` - Diagram showing the hierarchy of Makers and Checkers.

## Setup Instructions

### Prerequisites

- Python 3.x
- MongoDB
- Virtualenv (optional but recommended)

### Installation

1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
   cd customer_management_project
   ```

2. **Create and Activate Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB:**
   Ensure MongoDB is running and accessible. Import the database dump:
   ```sh
   mongorestore --uri="mongodb://localhost:27017/customer_management_db" deliverables/customer_management_db_dump/
   ```

5. **Run Migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create Superuser (optional):**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```sh
   python manage.py runserver
   ```

8. **Access the Application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/customer_management/login/` to log in.

## File Structure

```plaintext
customer_management_project/
│
├── customer_management/          # Django app
├── customer_management_project/  # Django project files
├── media/                        # Uploaded media files (photos, resumes)
├── templates/                    # HTML templates
├── static/                       # Static files (CSS, JS, etc.)
├── venv/                         # Virtual environment (optional, can be excluded)
├── db.sqlite3                    # SQLite database file (if used)
├── requirements.txt              # Python dependencies
├── manage.py                     # Django management script
│
├── deliverables/                 # Deliverables folder
│   ├── customer_management_db_dump.zip  # MongoDB database dump
│   ├── user_credentials.txt             # User credentials for Makers and Checkers
│   └── hierarchy_diagram.png            # Hierarchy diagram
│
├── README.md                     # Instructions for running the project
```

## User Credentials

The `user_credentials.txt` file inside the `deliverables/` directory contains the credentials for the Makers and Checkers.

## Notes

- Ensure that the media directory is properly set up to store uploaded photos and resumes.
- The application must be run in an environment where MongoDB is accessible.

## Troubleshooting

If you encounter any issues, ensure that:

- MongoDB is running and accessible.
- All Python dependencies are installed.
- The database has been correctly imported.

## Accessing the Repository

You can also access the project via the Git repository:

[GitHub Repository](https://github.com/your-username/customer_management_project)

---

Thank you for using the Customer Management Project. Enjoy!
```

Make sure to replace `<repository_url>` with the actual URL of your GitHub repository. This `README.md` provides all necessary details, including setup instructions, file structure, and links to both the zip file and the GitHub repository.