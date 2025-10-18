# Django URL Shortener

A simple and elegant URL Shortener built with **Django**.  
It allows users to shorten long URLs and easily redirect to the original address.

## Features

- Shorten any long URL into a unique short code  
- Redirects users to the original URL automatically  
- Manage all links via Django Admin  
- Clean, minimalist interface with responsive design  

---

## Installation & Setup

Follow these steps to run the project locally  

1. Clone the Repository  
```bash
git clone https://github.com/dimmuhamedsattarov/url_shortener.git
cd url_shortener
```

2. Create and Activate Virtual Environment  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Required Packages  
```bash
pip install -r requirements.txt
```

4. Apply Migrations  
```bash
python manage.py migrate
```

5. Run the Development Server  
```bash
python manage.py runserver
```

Then open your browser and visit: http://127.0.0.1:8000/

---

## Django Admin Access

- **Login**: `admin`
- **Password**: `MyStrongPass123`

Access the admin panel at: http://127.0.0.1:8000/admin/
