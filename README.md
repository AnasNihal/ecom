# 🛒 Ecom — Full Stack E-commerce Web App

A powerful and modern **E-commerce web application** built with:

- 🔧 **Backend:** Python Django
- 🎨 **Frontend:** React.js + Tailwind CSS
- 🛠️ **Database:** SQLite/PostgreSQL
- 🌐 **Authentication:** Django Auth / JWT (customizable)
- 💳 **Checkout:** Placeholder for payment integration (Razorpay/Stripe)

---

## 📸 Preview

![Ecom Preview](link-to-screenshot.png) <!-- Upload screenshot to repo or use external link -->

---

## 📂 Tech Stack

| Layer       | Technology               |
|-------------|--------------------------|
| Frontend    | React.js, Tailwind CSS   |
| Backend     | Django, Django REST Framework |
| Database    | SQLite / PostgreSQL      |
| Auth        | Django Auth / JWT        |
| Styling     | Tailwind CSS             |
| Deployment  | (Coming Soon)            |

---

## 🚀 Features

- 🛍️ Product Listing, Filtering, and Details
- 🧺 Add to Cart / Remove from Cart
- 👤 User Authentication & Authorization
- 📦 Order Management System (Admin + User View)
- 🧾 Django Admin Dashboard
- 💬 Scalable API backend with Django REST Framework

---

## 🔧 Setup Instructions

### Backend (Django)

```bash
# Clone the repo
git clone https://github.com/yourusername/ecom.git
cd ecom

# Create virtual environment & activate
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Start the server
python manage.py runserver
