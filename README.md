# Book Distribution Management System - Django Implementation

## Project Objectives

1. **Track Book Distribution Expenses:** Efficiently monitor and manage expenses related to book distribution.

2. **Increase Data Security and Availability:** Enhance the security and accessibility of book-related data for better management and decision-making.

3. **Customize and Automate Business Processes:** Tailor and automate various business processes to streamline book distribution operations.

## Your Challenge

Your challenge is to implement the following features in the Book Distribution Management System using Django and Pipenv:

### 1. CRUD View for Book Categories

Create a Django app and implement a CRUD (Create, Read, Update, Delete) view to manage book categories. Examples of categories include Business Analytics, Python, Data Science, and Math. This feature will enable users to add, view, edit, and delete book categories.

### 2. CRUD View for Book Information

Implement a CRUD view within the Django app to add and manage detailed book information. The information should include the title, author, publishing date, book category, and distribution expenses. Users should be able to add new books, view existing books, update book details, and delete books from the system.

### 3. Data Import from Spreadsheets ***** Coming Soon

Develop functionality to import existing data from spreadsheets into the Django application. This feature will facilitate the smooth transition of data from existing sources to the new Book Distribution Management System.

### 4. Report View for Distribution Expenses

Create a report view within the Django app that allows the team to analyze and view distribution expenses of books according to their categories. This feature is essential for gaining insights into how expenses are distributed across different book categories, aiding in better decision-making and resource allocation.

## Getting Started

To set up and run the Book Distribution Management System with Django and Pipenv, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/book_distribution_system.git
   ```

2. Navigate to the project directory and install dependencies using Pipenv.

   ```bash
   cd book-distribution-system-django
   pipenv install
   ```

3. Activate the virtual environment.

   ```bash
   pipenv shell
   ```

4. Apply migrations to set up the database.

   ```bash
   python manage.py migrate
   ```

5. Run the development server.

   ```bash
   python manage.py runserver
   ```

6. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).

## Contributing

If you'd like to contribute to the development of the Book Distribution Management System, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.
