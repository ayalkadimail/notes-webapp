# Project Notes – Flask Website with Authentication and Database

## 🗓️ Project Start Date: 02/07/2025

## 📁 Folder Structure (Initial)
NOTES_PYTHON
└── website
│   ├── auth.py
│   ├── __init__.py
│   ├── models.py
│   ├── __pycache__
│   │   └── __init__.cpython-312.pyc
│   ├── static
│   ├── templates
│   └── views.py
└── main.py



---

## 🧠 Learnings and Notes

# Flask Application Setup:

  - Flask apps are typically created using the application factory pattern inside a `create_app()` function located in `__init__.py`.
  - This pattern makes the app modular, reusable, and easier to test by centralizing setup and configuration.

Inside create_app():

  - Instantiate the Flask app with `Flask(__name__)`.
  - Configure important settings like `SECRET_KEY` for session and cookie security.

main.py:

  - Responsible for starting the application.
  - Imports the app factory: `from website import create_app`.
  - Calls `app.run(debug=True)` to launch the development server.
  - Uses `if __name__ == '__main__':` to ensure the app runs only when executed directly, not when imported.

Development Mode (`debug=True`):

  - Enables automatic server reloads when code changes.
  - Shows detailed error messages in the browser to aid debugging.



# Introducing Routes, Views, and Blueprints:

  Routes: 
    - URLs that users visit on your website (e.g., '/' for homepage).
    - When a user visits a route, the corresponding Python function runs and returns a response (like HTML).

  Views:
    - Python functions linked to routes that define what content or page the user sees.
    - For example, the 'home()' function in 'views.py' returns a simple HTML heading.

  Blueprints:
    - Flask’s way to organize routes and views into modular, reusable components.
    - Instead of putting all routes in one file, Blueprints let you split related routes logically (e.g., 'views' for general pages, 'auth' for authentication).
    - Each Blueprint works like a mini-application inside your main Flask app.
    - This keeps your project organized, scalable, and easier to maintain.

What We Did in Code:

  In views.py:
    - Created a Blueprint called 'views'.
    - Defined a route '/' (homepage) using '@views.route('/')'.
    - The 'home()' view returns a simple HTML string for testing.

  In auth.py:
    - Created a Blueprint called 'auth' for authentication routes.
    - Defined routes:
      - '/login': returns a placeholder "<p>Login</p>"
      - '/logout': returns a placeholder "<p>Logout</p>"
      - '/sign-up': returns a placeholder "<p>Sign Up</p>"

  In __init__.py:
    - Imported both Blueprints: 'views' and 'auth'.
    - Registered them on the Flask app with:
      - app.register_blueprint(views, url_prefix='/')
      - app.register_blueprint(auth, url_prefix='/')
    - The 'url_prefix=/' means routes inside each Blueprint are accessible directly at their defined URLs.


# Using Jinja2 Templates to Render Pages:

  - Created `base.html` as a base template to hold common layout and styling, including:
    - Bootstrap and FontAwesome CSS linked via CDN.
    - Custom navbar with a pink background using `.custom-navbar` CSS class.
    - Navbar links for Home, Login, Logout, and Sign Up.
    - JavaScript dependencies for Bootstrap’s interactive components.
    - Added a content placeholder block inside a Bootstrap container:
      - `<div class="container">{% block content %}{% endblock %}</div>`

  - Created `home.html` that:
    - Extends `base.html` to reuse the common layout.
    - Overrides the `{% block title %}` to set a custom page title ("Changed").
    - Defines the `{% block content %}` with page-specific content:
      - `<h1>Welcome to the Home Page</h1>`

  - Updated `views.py`:
    - Imported `render_template` from Flask.
    - Modified the `/` route (`home` function) to return `render_template("home.html")`.
    - This serves the `home.html` template when the homepage is visited.

  Key Points:

    - Jinja2’s `{% extends %}` allows template inheritance, so child templates reuse the base layout.
    - Blocks like `{% block title %}` and `{% block content %}` are placeholders that child templates override.
    - Wrapping the content block in a Bootstrap `.container` keeps content aligned and padded.
    - Using `render_template()` replaces returning raw HTML strings with rendering actual template files.
    - Templates are stored in the `templates/` folder by Flask convention.


# Creating Login and Sign-Up Pages with Templates:

  - Added two new templates in the `templates/` folder:
  
    - `login.html`:
        - Extends `base.html`.
        - Sets the page title to "Login".
        - Defines a content block with the heading: "Welcome to the Login Page".

    - `sign_up.html`:
        - Extends `base.html`.
        - Sets the page title to "Sign Up".
        - Defines a content block with the heading: "Welcome to the Sign Up Page".

  - Updated `auth.py` Blueprint routes to render these templates:

    - `/login`:
        - View function: `login()`
        - Returns `render_template("login.html")`.

    - `/sign-up`:
        - View function: `sign_up()`
        - Returns `render_template("sign_up.html")`.

    - `/logout`:
        - Temporarily redirects back to `home.html` for now (until logout functionality is added).

  Key Points:

    - Each authentication-related route now displays its own page using its respective template.
    - All templates inherit layout and navbar from `base.html`, keeping the site consistent.
    - Routing logic and templates are clearly separated using Blueprints for maintainability.


# Passing Data from Flask to Templates:

  - Flask’s `render_template()` allows passing variables to HTML templates.
  - Example:
      - In `auth.py`: 
        ```python
        return render_template("login.html", text="testing")
        ```
      - In `login.html`: 
        ```jinja
        {{ text }}
        ```
      - Output:
        ```
        Welcome to the Login Page
        testing
        ```

  - This allows you to display dynamic content like:
      - Usernames
      - Messages
      - Form data
      - Database results

  Key Concepts:

    - Variables passed to `render_template()` appear in the template as Jinja2 expressions.
    - Jinja2 uses double curly braces `{{ }}` to display variable values inside HTML.
    - Multiple values can be passed as keyword arguments:
      ```python
      render_template("page.html", name="Aya", age=20)
      ```
      And accessed in the template like:
      ```jinja
      Hello {{ name }}, you are {{ age }} years old.
      ```

  - This forms the basis of dynamic, user-specific web pages.


# Login and Sign-Up Forms with POST Handling:

  - Created two templates:
      - `login.html`
      - `sign_up.html`

  - Both templates:
      - Extend `base.html` for layout consistency.
      - Use `method="POST"` to submit sensitive form data securely to the same route.
      - Include a centered title (`<h3 align="center">`).
      - Use Bootstrap classes for styling (`form-group`, `form-control`, `btn`).
      - Buttons styled with custom inline CSS to match favorite color `#FFE2E2`.

  - Form Fields:

      - `login.html`:
          - **Email** (`type="email"`, `name="email"`)
          - **Password** (`type="password"`, `name="password"`)

      - `sign_up.html`:
          - **Email**, **First Name**, **Password**, **Password Confirm**
          - Uses distinct `name` attributes for each input field (e.g., `password1`, `password2`)

  - Route Configuration:

      - Updated `auth.py` to allow both `GET` and `POST` methods:
        ```python
        @auth.route('/login', methods=['GET', 'POST'])
        @auth.route('/sign-up', methods=['GET', 'POST'])
        ```

      - Why:
          - `GET` is used when the user first visits the page (to display the form).
          - `POST` is used when the user submits the form data to the server.

  Key Reminders:

      - Forms send data to the **same route** by default unless otherwise specified.
      - Always use `POST` when handling private data (like passwords).
      - Data is accessed in Flask using `request.form[...]` or `request.form.get(...)`.


# 🔐 Sign-Up Form Validation & Flash Messages:

  - Inside the `/sign-up` route:
      - Used `request.method == "POST"` to detect form submission.
      - Retrieved user input with `request.form.get(...)`.

  - Input fields handled:
      - `email`
      - `firstName`
      - `password1`
      - `password2`

  - Validation rules added:
      - Email must be at least 4 characters.
      - First name must be at least 2 characters.
      - Passwords must match.
      - Password must be at least 8 characters long.

  - Used `flash(message, category)` to send feedback to the user:
      - If any rule fails → flashed with category `"error"`.
      - If all inputs are valid → flashed with `"success"`.

  - Displaying flash messages in `base.html`:
      - Used `get_flashed_messages(with_categories=True)` to get both message and category.
      - Used Bootstrap alert boxes to style the messages:
          - `alert-danger` for errors
          - `alert-success` for success
      - Included a close (`×`) button in each alert.

  - Required Import:
      - Added `from flask import flash` to `auth.py`.

  🔥 Important Note:
      - Flash messages require a configured `SECRET_KEY` in the app:
        ```python
        app.config['SECRET_KEY'] = 'your-secret'
        ```

  ✅ Result:
      - User now receives clear and styled feedback when signing up.
      - Input validation prevents bad or insecure data from being processed.


# 🧠 Why We Use SQLAlchemy in Flask:

  - SQLAlchemy is a powerful and widely-used ORM (Object-Relational Mapper).
  - It allows us to interact with the database using **Python classes and objects** instead of raw SQL queries.

  ✔ Advantages:
      - Clean and readable syntax
      - Avoids repeating boilerplate SQL code
      - Works with multiple databases (SQLite, MySQL, PostgreSQL, etc.)
      - Integrates easily with Flask using `flask_sqlalchemy`
      - Works well with tools like Flask-Migrate for schema updates

  🔁 Alternatives:
      - Peewee → simpler, lighter ORM
      - Raw SQL → full control but less abstraction
      - Tortoise ORM → better for async frameworks
      - Pony ORM → readable, but less common
      - Django ORM → only used with Django (not Flask)

  ✅ Chose SQLAlchemy because it balances power, simplicity, and Flask compatibility.



# 📘 Flask Models & SQLAlchemy
intro: >
  In Flask, a model is a Python class that represents a table in a database.
  SQLAlchemy allows you to define these models and interact with your database
  using Python instead of raw SQL.
---

🧱 What is a Model?

definition: >
  A model is a Python class that inherits from `db.Model`. Each class variable 
  defines a column in the table.

uses:
  - Define your database schema.
  - Insert, update, and retrieve data using Python.
  - Avoid manual SQL queries.
---

🧾 Models in This Project
- User Model:
  class_name: User
  inherits: db.Model, UserMixin
    Represents a user of the app. Each user can have multiple notes.

- Note Model:
  class_name: Note
  inherits: db.Model
    Represents a note created by a user. Each note is linked to one user.
---

🔁 Relationship Types in SQLAlchemy
## One-to-Many:
  example: User → Notes
  setup:
    parent_model:
      - Define `notes = db.relationship('Note', backref='user', lazy=True)`
    child_model:
      - Define `user_id = db.Column(db.Integer, db.ForeignKey('user.id'))`
  result:
    - Access all notes: `user.notes`
    - Access the note's owner: `note.user`

## One-to-One:
  example: User → Profile
  setup:
    parent_model:
      - Define `profile = db.relationship('Profile', backref='user', uselist=False)`
    child_model:
      - Define `user_id = db.Column(db.Integer, db.ForeignKey('user.id'))`
  result:
    - Access profile: `user.profile`
    - Access user: `profile.user`

## Many-to-Many:
  example: Student ↔ Course
  setup:
    association_table:
      name: student_course
      definition: |
        student_course = db.Table('student_course',
          db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
          db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
        )
    models:
      Student:
        - Define `courses = db.relationship('Course', secondary=student_course, backref='students')`
      Course:
        - No extra definition needed unless adding specific fields
  result:
    - Access student’s courses: `student.courses`
    - Access course’s students: `course.students`
---
🔧 SQLAlchemy Concepts
foreign_key:
  definition: >
    A field that links a row in one table to a row in another table.
  example: `db.Column(db.Integer, db.ForeignKey('user.id'))`

relationship:
  definition: >
    Allows navigation between linked models (e.g., user.notes or note.user).
  parameters:
    - backref: Adds a reverse reference automatically (e.g., note.user)
    - lazy:
        select: Loads data when accessed
        dynamic: Returns a query for filtering
---
📌 Best Practices
  - Place all models in `models.py` to keep things organized.
  - Use `db.create_all()` or Flask-Migrate to generate your database.
  - Don’t store raw passwords — hash them!
  - Use `UserMixin` to integrate with `flask_login`.


# - step: Setting up the database with SQLAlchemy
  description: |
    Set up the SQLite database using SQLAlchemy and created the models for User and Note. Ensured the database is created inside the correct folder using an absolute path.

  tools:
    - Flask
    - Flask-SQLAlchemy
    - SQLite
    - Python's os and path modules

  config:
    database_name: database.db
    database_location: website/database.db
    secret_key: "secret"
    sqlalchemy_uri: "sqlite:///<absolute_path_to>/website/database.db"

  key_changes:
    - Used SQLAlchemy to handle the database layer and model definitions.
    - Used `db.create_all()` to create the DB schema.
    - Ensured the database file is created in the correct location using:
        DB_PATH = path.join(path.dirname(__file__), DB_NAME)
    - Replaced relative URI with an absolute one to avoid Flask defaulting to /instance.
    - Wrapped `db.create_all()` inside `with app.app_context()` for compatibility with SQLAlchemy v3+.

  result:
    - ✅ Database successfully created in: website/database.db
    - ✅ Tables for User and Note created on first run
    - ✅ No more issues with Flask defaulting to /instance folder


# # 🧠 User Sign-Up & Secure Account Creation

- step: Handle user sign-up with database insertion
  route: /sign-up
  method: POST
  tools:
    - request.form
    - flash
    - werkzeug.security.generate_password_hash
    - SQLAlchemy (db.session)
  logic:
    - Collect user input: email, first name, password1, password2
    - Validate:
        - Email length ≥ 4
        - First name length ≥ 2
        - Passwords match
        - Password length ≥ 8
    - On success:
        - Hash the password securely:
          method: pbkdf2:sha256
          example: hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
        - Create a new User object:
            - email
            - first_name
            - hashed password
        - Add and commit the user to the database:
            - db.session.add(user)
            - db.session.commit()
        - Flash a success message
        - Redirect to home page
  result:
    - ✅ New users are stored in the database securely
    - ✅ Passwords are hashed and not stored in plain text
    - ✅ User receives visual feedback via flash message
  imports:
    - from .models import User
    - from werkzeug.security import generate_password_hash
    - from . import db


# # 🔐 Login Functionality & Improved Sign-Up Validation

- step: Handle user login via form
  route: /login
  method: POST
  logic:
    - Collect email and password from form
    - Query the database: `User.query.filter_by(email=email).first()`
    - If user exists:
        - Check hashed password using `check_password_hash(user.password, password)`
        - On success:
            - Flash "Logged in successfully!"
            - Redirect to home
        - On failure:
            - Flash "Incorrect password, try again."
    - If user does not exist:
        - Flash "Email does not exist."
  result:
    - ✅ User receives accurate feedback
    - ✅ Passwords are securely checked using hashing
    - ✅ Redirects only if credentials are valid
  imports:
    - from werkzeug.security import check_password_hash

- step: Prevent duplicate emails on sign-up
  file: auth.py
  location: Inside /sign-up route before inserting new user
  logic:
    - Query database: `User.query.filter_by(email=email).first()`
    - If user exists:
        - Flash "Email already exists."
        - Do not proceed with creation
  result:
    - ✅ Prevents users from registering with the same email
    - ✅ Ensures email uniqueness


# # 🔐 Flask-Login Integration – User Sessions & Access Control

- step: Integrate Flask-Login for session management
  purpose: >
    Track logged-in users, protect private routes, and provide access to current user info.
  tools:
    - Flask-Login
    - `UserMixin` (in User model)
  file: models.py
  change:
    - Inherit `UserMixin` in `User` model to enable session tracking.
    - Enables methods like `is_authenticated`, `is_active`, `get_id()`, and use of `current_user`.

- step: Initialize Login Manager
  file: __init__.py
  location: After `create_database(app)`
  code: |
    from flask_login import LoginManager

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # redirect to login if not authenticated
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))  # loads user by ID for session
  result:
    - ✅ Tracks user sessions
    - ✅ Automatically redirects to login if not authenticated
    - ✅ `current_user` available globally

- step: Login Function – Set User Session
  file: auth.py
  change:
    - After checking password in `/login`, log user in:
      ```python
      login_user(user, remember=True)
      ```
  result:
    - ✅ Starts a session for the user
    - ✅ `current_user` is now populated

- step: Logout Function – End Session
  file: auth.py
  change:
    - Updated `/logout` route:
      ```python
      @login_required
      def logout():
          logout_user()
          return redirect(url_for('auth.login'))
      ```
  result:
    - ✅ Secure logout only allowed when user is logged in
    - ✅ Session is cleared on logout

- step: Protect Routes with @login_required
  file: views.py
  route: /
  change:
    - Add decorator:
      ```python
      @login_required
      def home():
          return render_template("home.html")
      ```
  result:
    - ✅ Home page is now protected
    - ✅ Only accessible to logged-in users
    - ✅ Redirects to `/login` if unauthenticated

- step: Use current_user
  available_in:
    - Any template
    - Any view function
  description: >
    Provides access to the currently logged-in user.
    Can access fields like `current_user.email`, `current_user.id`, etc.
  example_usage:
    - In Python: `current_user.first_name`
    - In Jinja: `{{ current_user.first_name }}`



# # ✅ Notes Update – User-Specific Notes + Delete Logic

## 🧩 New Features

- Allow users to:
  - Add notes (stored in database)
  - View only their notes
  - Delete their own notes with a button

---

## 🧠 Concepts Introduced

add_notes:
  description: |
    Users can now submit notes through a form on the home page.
    These notes are stored in the database and linked to the currently logged-in user.
  logic:
    - Check if POST method
    - Get note content from form
    - If valid, create a Note instance with current_user.id as foreign key
    - Commit to DB
  route:
    path: /
    method: [GET, POST]
    decorator: @login_required
  template:
    - Iterates over `user.notes` to display notes
    - Includes delete button for each note
    - Uses Bootstrap list styles

delete_notes:
  description: |
    Users can delete their own notes. This is done through an AJAX request
    to the `/delete-note` endpoint, which expects a note ID in JSON.
  route:
    path: /delete-note
    method: POST
  logic:
    - Parse JSON body using `json.loads(request.data)`
    - Query for note by ID
    - Check if current user owns the note
    - If so, delete and commit
    - Return empty JSON response
  tools:
    - json
    - jsonify
    - Flask routes and models

---

## ✨ New Code Snippets

### 🔐 `views.py`

```python
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
    return jsonify({})
