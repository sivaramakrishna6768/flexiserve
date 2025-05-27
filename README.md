# 🚀 FlexiServe – CI/CD Enabled Web App

FlexiServe is a modular full-stack web application built with **FastAPI** (backend) and **React** (frontend), using **PostgreSQL** as the database. The project is containerized with Docker, features CI/CD integration using GitHub Actions, and is deployed to Render.

---

## 📁 Project Structure

```
flexiserve/
├── backend/   # FastAPI backend with PostgreSQL + Alembic
├── frontend/  # React frontend created with Create React App
```

---

## 🛠️ Technologies Used

- **Backend:** FastAPI, SQLAlchemy, Alembic
- **Frontend:** React.js (Create React App)
- **Database:** PostgreSQL
- **DevOps:** Docker, Docker Compose, GitHub Actions (CI/CD)
- **Deployment:** Render

---

## ⚙️ Getting Started

### 🧾 Prerequisites

- Docker & Docker Compose installed
- Node.js and npm (for local frontend dev)

---

### 🔧 Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/sivaramakrishna6768/flexiserve.git
cd flexiserve
```

2. **Run with Docker Compose:**

```bash
cd backend
docker compose up --build
```

3. **Access the app locally:**

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 API Testing

Use the FastAPI Swagger UI at `/docs` to test your backend endpoints:

- `GET /users` → Fetch all users
- `POST /users` → Add a new user

---

## 📦 Frontend – React App

The React app is located in the `frontend/` directory.

To run it independently (non-Docker), do:

```bash
cd frontend
npm install
npm start
```

To build for production:

```bash
npm run build
```

---

## 🚀 Deployment (Optional)

You can deploy the full-stack application to **Render** using:

- Render web service (for FastAPI)
- Render static site (for React)
- PostgreSQL instance (Render or external)

---

## 🙌 Credits

This project was built by **Siva Ramakrishna Palaparthy** as a CI/CD-enabled full-stack portfolio piece to demonstrate end-to-end application design and deployment.
