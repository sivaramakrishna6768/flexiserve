# FlexiServe – CI/CD Enabled Web App

**FlexiServe** is a modular full-stack web application built with **FastAPI** (backend), **React** (frontend), and **PostgreSQL** (database). It enables scalable API-driven workflows and demonstrates modern DevOps practices with **Docker**, **GitHub Actions**, and **Render**.

---

## 🔧 Features

- 🧩 Modular full-stack design with FastAPI and React
- 🗃️ PostgreSQL database with Alembic for schema migrations
- 🚀 REST API for user creation and listing
- 🐳 Dockerized backend and frontend
- ⚙️ CI/CD pipeline with GitHub Actions for build/test/deploy
- 🌐 Deployed on Render (separate services for frontend and backend)

---

## 📁 Project Structure

flexiserve/
│
├── backend/ # FastAPI app
│ ├── app/
│ │ ├── models/
│ │ ├── routers/
│ │ ├── schemas/
│ │ └── database.py
│ ├── alembic/ # Alembic migrations
│ ├── start.sh
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/ # React app
│ ├── src/
│ ├── public/
│ ├── Dockerfile
│ ├── package.json
│ └── build/ # Created after npm run build
│
└── .github/workflows/ # GitHub Actions CI/CD configs

---

## ⚙️ Technologies Used

- **Backend**: FastAPI, SQLAlchemy, Alembic, PostgreSQL
- **Frontend**: React.js (Create React App)
- **DevOps**: Docker, GitHub Actions, Render

---

## 🚀 Live Demo

- 🌐 Frontend: [https://flexiserve-frontend.onrender.com](https://flexiserve-frontend.onrender.com)  
- 🛠️ Backend (Swagger UI): [https://flexiserve-backend.onrender.com/docs](https://flexiserve-backend.onrender.com/docs)

---

## 🚀 Deployment

### Backend (FastAPI)

```bash
cd backend
docker build -t flexiserve-backend .
# Deployed on Render with Docker; also supports local run
```

### Frontend (React)

```bash
cd frontend
npm install
npm run build
# Deployed as a static site on Render using the build/ directory
```
---

🔄 CI/CD

- GitHub Actions triggers build/test/deploy on push to main
- Docker containers are built and deployed to Render
- Frontend and backend services are managed independently

---

📬 API Endpoints

- Method	Endpoint	Description
- GET	/users/	List all users
- POST	/users/	Create new user

---

🧪 How to Test

- Visit frontend URL: https://flexiserve-frontend.onrender.com
- Submit name and email
- Confirm data via backend Swagger UI : https://flexiserve-backend.onrender.com/docs

---

## 🙌 Credits

This project was built by **Siva Ramakrishna Palaparthy** as a CI/CD-enabled full-stack portfolio piece to demonstrate end-to-end application design and deployment.

---
