
# Customer Management Project

## Description

This project is a customer management system built using Django and MongoDB. It allows two types of users: Makers and Checkers. Makers can upload customer data, including photos and resumes, while Checkers can view, approve, or decline the customer data uploaded by the Makers under their supervision.

## Features

- **Makers:**
  - Upload customer data (photo and resume).
  - View the status of all uploaded customers.

- **Checkers:**
  - View customer data uploaded by their assigned Makers.
  - Approve or decline customer data.
  - View the status of all customers uploaded by their assigned Makers.

## Technical Specifications

- **Language:** Python
- **Framework:** Django
- **Database:** MongoDB

## Deliverables

- **Project Folder:** Ready to run, that would render all the required pages.
- **Database Dump:** Included in the `deliverables` folder.
- **User Credentials:** Provided in the `deliverables` folder.
- **Hierarchy Diagram:** Included in the `deliverables` folder, detailing which Makers come under which Checkers.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/popzon99/customer_management_project.git
   cd customer_management_project
   ```

2. **Set Up Virtual Environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB:**

   Ensure MongoDB is installed and running on your local machine.

5. **Load Database Dump:**

   ```sh
   mongorestore --uri="mongodb://localhost:27017/customer_management_db" deliverables/customer_management_db_dump
   ```

6. **Run Migrations:**

   ```sh
   python manage.py migrate
   ```

7. **Run the Server:**

   ```sh
   python manage.py runserver
   ```

## Project Structure

```plaintext
customer_management_project/
├── customer_management/          # Django app
├── customer_management_project/  # Django project files
├── media/                        # Uploaded media files (photos, resumes)
├── templates/                    # HTML templates
├── static/                       # Static files (CSS, JS, etc.)
├── venv/                         # Virtual environment (optional, can be excluded)
├── db.sqlite3                    # SQLite database file (if used)
├── requirements.txt              # Python dependencies
├── manage.py                     # Django management script
├── README.md                     # Instructions for running the project
├── deliverables/                 # Deliverables folder
│   ├── customer_management_db_dump/   # MongoDB database dump folder
│   ├── user_credentials.txt            # User credentials for Makers and Checkers
│   └── hierarchy_diagram.png           # Hierarchy diagram
```

## User Credentials

You can find the user credentials for Makers and Checkers in the `deliverables/user_credentials.txt` file.

## Hierarchy Diagram

A hierarchy diagram detailing which Makers come under which Checkers is included in the `deliverables/hierarchy_diagram.png` file.

## Contact

For any queries or issues, please contact:

- Name: popson sabu
- Email: popsonsabu25@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
```

You can adjust the contact information and any other details as necessary before finalizing the README file.