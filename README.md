# Django URL Shortener

A powerful URL shortener web application built with Django that transforms long URLs into short, manageable links.

## Features

- Convert long URLs into short, unique codes
- Automatic redirection to original URLs
- Admin dashboard for full management
- Click analytics and usage tracking

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/dimmuhamedsattarov/url_shortener.git
```

2. **Navigate to project directory**
```bash
cd url_shortener
```

3. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Start development server**
```bash
python manage.py runserver
```
## Basic Usage

### Shorten URL via Web Interface
Visit http://127.0.0.1:8000/ and enter your long URL to get a shortened version.

## Admin Access

- **Username**: `admin`
- **Password**: `MyStrongPass123`

Access the admin panel at: http://127.0.0.1:8000/admin/



