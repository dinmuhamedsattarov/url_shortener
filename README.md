# 🌐 Django URL Shortener

A simple and elegant URL Shortener built with **Django**.  
It allows users to shorten long URLs and easily redirect to the original address.

---

## 🚀 Features

- Shorten any long URL into a unique short code  
- Redirects users to the original URL automatically  
- Manage all links via Django Admin  
- Clean, minimalist interface with responsive design  

---

## 🛠️ Installation & Setup

Follow these steps to run the project locally 

1️⃣ Clone the Repository
git clone https://github.com/dinmuhamedsattarov/url_shortener.git
cd url_shortener

2️⃣ Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Required Packages
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Run the Development Server
python manage.py runserver

Then open your browser and visit:
http://127.0.0.1:8000/

