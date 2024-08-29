# **Full-Stack User Management System**

This project is a full-stack user management system built with Django (backend) and React (frontend). It includes features like user registration, login, password reset, and email verification.

## **Table of Contents**

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Backend Setup (Django)](#backend-setup-django)
5. [Frontend Setup (React)](#frontend-setup-react)
6. [Environment Variables](#environment-variables)
7. [Running the Application](#running-the-application)
8. [Testing the Application](#testing-the-application)
9. [API Endpoints](#api-endpoints)
10. [Common Issues](#common-issues)
11. [Contributing](#contributing)
12. [License](#license)

## **Project Structure**

```plaintext
project-root/
│
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── users/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── models.py
│   │   └── ...
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── SignUp.jsx
    │   │   ├── ForgotPassword.jsx
    │   │   ├── ResetPassword.jsx
    │   │   └── ...
    │   ├── App.jsx
    │   ├── index.js
    │   └── ...
    ├── public/
    ├── package.json
    └── vite.config.js
```

## **Prerequisites**

- **Python 3.8+** and **pip**
- **Node.js 14+** and **npm** (or **yarn**)
- **Django** (installed via `pip`)
- **React** (installed via `npm` or `yarn`)

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/full-stack-user-management.git
cd full-stack-user-management
```

## **Backend Setup (Django)**

### **1. Create and Activate a Virtual Environment**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Apply Migrations**

```bash
python manage.py migrate
```

### **4. Create a Superuser**

```bash
python manage.py createsuperuser
```

### **5. Run the Development Server**

```bash
python manage.py runserver
```

The backend will be running on `http://127.0.0.1:8000`.

## **Frontend Setup (React)**

### **1. Install Dependencies**

```bash
cd frontend
npm install
# or
yarn install
```

### **2. Configure the API Endpoint**

Ensure the API base URL in your frontend code points to the correct Django backend URL.

### **3. Run the Development Server**

```bash
npm run dev
# or
yarn dev
```

The frontend will be running on `http://localhost:5173`.

## **Environment Variables**

Both the backend and frontend require certain environment variables. Here’s a list:

### **Backend (`.env` in the `backend` directory):**

```plaintext
SECRET_KEY=your-django-secret-key
DEBUG=True  # Set to False in production
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
```

### **Frontend (`.env` in the `frontend` directory):**

```plaintext
VITE_API_BASE_URL=http://127.0.0.1:8000/api/
```

## **Running the Application**

1. **Start the backend server**:
   - Ensure you’re in the `backend` directory and your virtual environment is activated.
   - Run `python manage.py runserver`.

2. **Start the frontend server**:
   - Ensure you’re in the `frontend` directory.
   - Run `npm run dev` or `yarn dev`.

Open your browser and navigate to `http://localhost:5173`.

## **Testing the Application**

### **Manual Testing**

1. **User Registration**:
   - Go to `/signup`.
   - Register a new user with a unique email and password.

2. **Login**:
   - Go to `/login`.
   - Log in with the registered email and password.

3. **Forgot Password**:
   - Go to `/forgot-password`.
   - Enter the registered email and submit.

4. **Password Reset**:
   - Check the email for the reset link or simulate getting the token.
   - Navigate to the reset link (`/reset-password/<uidb64>/<token>`).
   - Enter and confirm the new password.

### **Automated Testing**

For end-to-end (E2E) testing, consider using **Cypress**:

1. **Install Cypress**:
   ```bash
   npm install cypress --save-dev
   ```

2. **Run Cypress**:
   ```bash
   npx cypress open
   ```

3. **Write tests** in `cypress/e2e/` to cover all critical user flows.

## **API Endpoints**

### **Authentication**

- **POST** `/api/users/register/` - Register a new user.
- **POST** `/api/users/login/` - Log in a user.
- **POST** `/api/users/logout/` - Log out the current user.
- **POST** `/api/users/forgot-password/` - Send a password reset email.
- **POST** `/api/users/reset-password/<uidb64>/<token>/` - Reset the password using a token.

## **Common Issues**

- **CORS Errors**: Ensure CORS is configured correctly in your Django settings.
- **Email Sending**: If you’re testing locally, use `django.core.mail.backends.console.EmailBackend` to print emails to the console instead of sending them.

## **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request. Ensure that all new code follows the existing coding conventions and passes any tests.

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.
