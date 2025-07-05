# 📝 Notes Web Application

## 🔍 Overview

This is a full-stack web application built with **Flask**, a lightweight Python web framework, and integrated with a **Firefox browser extension**. It allows users to create, edit, and manage personal notes securely with login and signup functionalities. The extension provides a convenient way to access notes directly from the browser.

---

## 📁 Project Structure

```
├── WebSites/
│   ├── templates/
│   │   ├── base.html        # Base layout template
│   │   ├── home.html        # Homepage
│   │   ├── login.html       # Login page
│   │   ├── signup.html      # Signup page
│   │   ├── edit_notes.html  # Note editing interface
│   ├── __init__.py          # Flask app factory
│   ├── auth.py              # Authentication routes and logic
│   ├── models.py            # Database models (SQLAlchemy)
│   ├── views.py             # Core application routes and logic
│
├── notes_extension/
│   ├── manifest.json        # Firefox extension manifest
│   ├── popup.html           # HTML for the popup window
│   ├── popup.js             # JS for popup functionality
│
├── main.py                  # Entry point for running the Flask app
```

---

## ✨ Features

* ✅ User Authentication (Signup & Login)
* 📝 Create, Edit, and Manage Notes
* 💾 SQLite database integration via Flask-SQLAlchemy
* 🧩 Firefox Extension for quick note access
* 📱 Responsive and lightweight UI

---

## 🛠️ Technologies Used

| Layer         | Tools/Frameworks                     |
| ------------- | ------------------------------------ |
| **Backend**   | Flask, Flask-SQLAlchemy, Flask-Login |
| **Frontend**  | HTML, JavaScript                     |
| **Database**  | SQLite                               |
| **Extension** | Firefox WebExtension API             |
| **Language**  | Python 3.12.3                          |

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python 3.12.3
* `pip` (Python package manager)
* Firefox Browser

### 🐍 Backend Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ayalkadimail/notes-webapp.git
   cd notes-webapp
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install flask flask-sqlalchemy flask-login
   ```

4. **Run the application:**

   ```bash
   python main.py
   ```

   The app will be accessible at **[http://localhost:5000](http://localhost:5000)**

---

### 🧩 Firefox Extension Setup

1. Open Firefox and go to:
   `about:debugging#/runtime/this-firefox`

2. Click **"Load Temporary Add-on"**

3. Select the `manifest.json` file inside the `notes_extension/` folder.

4. The extension will now appear in your toolbar.

---

## 🧭 Usage

### 🌐 Web App

* Navigate to `http://localhost:5000`
* Sign up or log in
* Create, view, and edit notes from your personal dashboard

### 🧩 Browser Extension

* Click the extension icon in the Firefox toolbar
* Use the popup to **quickly view or add notes**
* All changes are synced with the web app

---

## Author

Created by AYA AL KADIRI

## 🔗 Repository

👉 GitHub: notes-webapp


---

Let me know if you'd like to turn this into a GitHub Pages landing page or add installation instructions for production later.

