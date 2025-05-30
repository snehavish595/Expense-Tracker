﻿
# 💰 Expense Tracker

A web-based **Expense Tracker** built using **Django** and **Tailwind CSS** that allows users to add, edit, and delete expenses. It displays data visually using pie charts and line charts for insightful tracking over days and categories.

---

## 🚀 Features

- Add, Edit, Delete Expenses  
- View all expenses in a clean tabular layout  
- Track total spending for:
  - Last 7 days
  - Last 30 days
  - Last 365 days
- Visualizations using Chart.js:
  - Daily expense trends (Line Chart)
  - Category-wise expense distribution (Pie Chart)
- Data aggregation by:
  - Date (Last 30 Days)
  - Category

---

## 🛠️ Tech Stack

- **Backend**: Django  
- **Frontend**: HTML, Tailwind CSS, Chart.js  
- **Database**: SQLite (default for Django)

---

## 📂 Folder Structure

<pre>
expense-tracker/
├── myapp/
│   ├── templates/
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── edit.html
│   ├── static/
│   │   └── myapp/
│   │       ├── images/
│   │       │   ├── wallet.png
│   │       │   ├── edit.png
│   │       │   └── delete.png
│   │       └── style.css / styles.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── project_root/
│   └── urls.py
├── db.sqlite3
├── manage.py
└── README.md
</pre>

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

### 5. Access the App

Visit: [http://localhost:8000](http://localhost:8000)

---

## 📊 Screenshots

![screenshot1.png](myapp/static/myapp/screenshots/screenshot1.png)
![screenshot2.png](myapp/static/myapp/screenshots/screenshot2.png)
![screenshot3.png](myapp/static/myapp/screenshots/screenshot3.png)
![screenshot4.png](myapp/static/myapp/screenshots/screenshot4.png)

---

## ✨ Future Enhancements

- User authentication (Login/Signup)  
- Export expenses to CSV/PDF  
- Responsive design improvements  
- Filter/search expenses by category or date  

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Sneha Vishwakarma**  
Software Developer  
[LinkedIn](https://www.linkedin.com/in/snehavish595/)
