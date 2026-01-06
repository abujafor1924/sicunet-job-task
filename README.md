
# Sicunet Django Project


---

## Table of Contents
1. [Requirements](#requirements)
2. [Setup Instructions](#setup-instructions)
3. [Run Development Server](#run-development-server)
4. [Run Tests](#run-tests)
5. [GitHub Actions CI](#github-actions-ci)
6. [Notes](#notes)

---

## Requirements

- Python 3.12+  
- pip  
- Git  



## Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd sicunet-job-task
````

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* On Linux/macOS:

```bash
source venv/bin/activate
```

* On Windows (cmd):

```bash
venv\Scripts\activate
```

4. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

5. **Apply database migrations**

```bash
cd sicunet
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser (optional, for admin)**

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## Run Development Server

```bash
python manage.py runserver
```

* The server will run by default at `http://127.0.0.1:8000/`

---

## Run Tests

```bash
python manage.py test
```

* All apps’ tests will be executed.




