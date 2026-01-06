
# Sicunet Django Project

---

## Table of Contents

1. [Requirements](#requirements)
2. [Setup Instructions (Local)](#setup-instructions-local)
3. [Run Development Server (Local)](#run-development-server-local)
4. [Run Project with Docker](#run-project-with-docker)
5. [Run Tests](#run-tests)
6. [GitHub Actions CI](#github-actions-ci)
7. [Notes](#notes)

---

## Requirements

* Python 3.12+
* pip
* Git
* Docker & Docker Compose (for Docker setup)

---

## Setup Instructions (Local)

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd sicunet-job-task
```

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

## Run Development Server (Local)

```bash
python manage.py runserver
```

* The server will run by default at: `http://127.0.0.1:8000/`

---

## Run Project with Docker

If you want to run the project using Docker (no need to install Python locally):

1. **Build and start containers**

```bash
docker-compose up --build
```

* Django server will run at: `http://0.0.0.0:8000/`
* Access it in your browser as: `http://localhost:8000/`

2. **Stop containers**

```bash
docker-compose down
```

3. **Run Django commands inside Docker**

```bash
docker-compose run --rm app python manage.py migrate
docker-compose run --rm app python manage.py createsuperuser
```

> Replace `app` with your service name from `docker-compose.yml` if different.

4. **View logs**

```bash
docker-compose logs -f
```

---

## Run Tests

```bash
python manage.py test
```
## Main Project Run Test
```bash
python sicunet/manage.py test access_control
```

* All apps’ tests will be executed.

If using Docker:

```bash
docker-compose run --rm web sh -c "python sicunet/manage.py test access_control"
```


