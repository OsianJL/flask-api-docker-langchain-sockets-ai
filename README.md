# Flask API with PostgreSQL – Fully Dockerized 🐳

This is a starter template for building robust Flask APIs using Docker for both the **API** and **PostgreSQL**. It's ideal for scalable development and easy team collaboration.

## 🚀 Features

- Python 3.11 + Flask 2.3
- PostgreSQL 16 (Dockerized)
- SQLAlchemy ORM
- Flask-Migrate (Alembic)
- Flask-Bcrypt (password hashing)
- Flask-JWT-Extended (authentication-ready)
- Environment variables via `.env`
- Migrations already initialized with a basic `User` model

## 📦 Requirements

- [Docker](https://www.docker.com/products/docker-desktop/) installed and running
- Git (to clone the project)

## 🧑‍💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2. Create your .env file
Create a .env file in the root of the project:

ini
Copiar
Editar
DATABASE_URL=postgresql://flaskuser:flaskpassword@db:5432/flaskdb
JWT_SECRET_KEY=your-secret-key
You can use .env.example as a reference.

3. Start the project with Docker
bash
Copiar
Editar
docker-compose up
On first run (or if you change dependencies), use:

bash
Copiar
Editar
docker-compose up --build
Once running, open your browser at http://localhost:5000 to confirm the API is live.

🔐 Registering a User
Send a POST request to:

bash
Copiar
Editar
POST http://localhost:5000/register
Body example:

json
Copiar
Editar
{
  "email": "your@email.com",
  "password": "yourPassword123"
}
If successful, the response will be:

json
Copiar
Editar
{
  "message": "User created successfully"
}
The user will be stored in the PostgreSQL database with a hashed password.

🛠 Project Structure
arduino
Copiar
Editar
├── app/
│   ├── models/
│   │   └── user.py
│   ├── config/
│   │   └── config.py
│   ├── extensions/
│   │   └── extensions.py
│   └── __init__.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .dockerignore
├── run.py
└── README.md
🧪 Migrations
Migrations are already set up with a users table. If you need to reset or add models:

bash
Copiar
Editar
# Get inside the API container
docker-compose exec api bash

# Then run:
flask db migrate -m "your message"
flask db upgrade
🧼 Useful Commands

Action	Command
Start the project	docker-compose up
Rebuild after dependency change	docker-compose up --build
Stop containers	docker-compose down
Enter API container	docker-compose exec api bash
Apply migrations	flask db migrate && flask db upgrade
🧑‍🎓 Author
Made by @OsianJL