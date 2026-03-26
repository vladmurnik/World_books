# 📚 Django Library Catalog Project

## Overview

This project is a **Django-based web application** for managing a library catalog. It allows you to store and manage information about books, authors, genres, languages, and book instances (copies), as well as track borrowed books by users.

---

## 🚀 Features

### 📖 Books

* Create, update, delete books (CRUD via class-based views)
* View book list with pagination
* Detailed book view
* Assign:

  * Genre
  * Language
  * Multiple authors
* Store summary and ISBN

### ✍️ Authors

* Add authors via custom form
* Edit author data manually (function-based view)
* Delete authors
* Display author list with pagination

### 📦 Book Instances

* Track physical copies of books
* Assign:

  * Status (e.g. available, borrowed)
  * Borrower (linked to user)
  * Due date
* Detect overdue books automatically

### 👤 User Features

* Authentication support
* Logged-in users can view borrowed books
* Session-based visit counter on homepage

---

## 🗂 Project Structure

### Models

* **Genre** – Book categories
* **Language** – Language of the book
* **Author** – Author details
* **Book** – Main book entity
* **Status** – Book availability status
* **BookInstance** – Individual copy of a book

---

### Views

#### Class-Based Views

* `BookCreate` – Create book
* `BookUpdate` – Update book
* `BookDelete` – Delete book
* `BookListView` – List books
* `BookDetailView` – Book details
* `AuthorListView` – List authors
* `LoanedBooksByUserListView` – Books borrowed by current user

#### Function-Based Views

* `index` – Homepage with statistics
* `create` – Create author
* `edit1` – Edit author
* `delete` – Delete author
* `autors_add` – Author list + form

---

### Forms

* `AuthorsForm`

  * Handles author creation
  * Uses HTML5 date inputs

---

### Admin Panel

* Custom admin configurations:

  * `AuthorAdmin` – structured author editing
  * `BookAdmin` – inline book instances
  * `BookInstanceAdmin` – filters and grouped fields
* Registered models:

  * Genre, Language, Status

---

## 📊 Homepage Statistics

The main page displays:

* Total number of books
* Total book copies
* Available copies
* Number of authors
* Number of visits (session-based)

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd project-folder
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🔐 Authentication

* Uses Django’s built-in `User` model
* Login required for viewing borrowed books

---

## 🧠 Key Concepts Used

* Django ORM relationships:

  * `ForeignKey`
  * `ManyToManyField`
* Class-Based Views (CBV)
* Function-Based Views (FBV)
* Django Admin customization
* Pagination
* Sessions
* Form handling

---

## 📌 Notes

* Some views (like author editing) use manual POST handling instead of Django forms
* Status filtering uses numeric values (`status__exact='2'`) — ensure statuses are consistent in DB
* URL paths like `/authors_add/` should match your `urls.py`

---

## 🛠 Possible Improvements

* Replace manual forms with `ModelForm`
* Add validation and error handling
* Improve URL routing with `reverse()`
* Add REST API (Django REST Framework)
* Improve UI with Bootstrap or Tailwind
* Add permissions (admin vs user)

---

## 📄 License

This project is for educational purposes. You can modify and use it freely.
