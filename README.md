# Online Library Management System

This project is a Django web application designed to manage an online library system. It allows administrators to manage books, authors, and their borrowing records. The application includes features for adding books and authors, assigning books to authors, and exporting library data to an Excel sheet.

## Features

- **Manage Books**: Add, edit, and delete books in the library.
- **Manage Authors**: Add, edit, and delete authors associated with the books.
- **Borrow Records**: Track which users have borrowed which books.
- **Data Export**: Export library data to an Excel sheet for reporting and analysis.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd online-library
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage books, authors, and borrow records.
- Use the provided forms to add or edit entries.
- Export data using the export functionality integrated into the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
