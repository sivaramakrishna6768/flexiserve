# FlexiServe – CI/CD Enabled User Management App

FlexiServe is a full-stack user management dashboard built with FastAPI, PostgreSQL, and React. It allows you to add and view users using a clean frontend interface, backed by a robust API and database infrastructure. The project is CI/CD-enabled and deployed on [Render](https://render.com) with GitHub Actions for automated builds and deployments.

## 🌐 Live Deployment

- **Frontend**: [Visit Frontend](https://flexiserve-frontend.onrender.com)
- **Backend (Swagger UI)**: [Visit API Docs](https://flexiserve-backend.onrender.com/docs)

## 🚀 Features

- Add and fetch users through a user-friendly interface.
- RESTful backend with FastAPI.
- PostgreSQL integration with Alembic migrations.
- Dockerized frontend and backend.
- CI/CD pipeline with GitHub Actions.
- Deployed on Render using free-tier services.

## 🧰 Tech Stack

- **Frontend**: React, HTML/CSS, JavaScript
- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Database**: PostgreSQL (hosted on Render)
- **DevOps**: Docker, GitHub Actions, Render
- **Migrations**: Alembic

## 📁 Project Structure

```
flexiserve/
│
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── main.py
│   ├── alembic/
│   └── Dockerfile
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js
│       └── index.js
│   └── Dockerfile
│
└── README.md
```

## ⚙️ Setup Instructions

### 🐳 Dockerized Local Development

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/flexiserve.git
   cd flexiserve
   ```

2. **Build and run the backend locally**  
   ```bash
   cd backend
   docker build -t flexiserve-backend .
   docker run -p 8000:8000 --env-file .env.local flexiserve-backend
   ```

3. **Build and run the frontend locally**  
   ```bash
   cd frontend
   docker build -t flexiserve-frontend .
   docker run -p 3000:3000 flexiserve-frontend
   ```

### 🧪 Testing the API

Go to [http://localhost:8000/docs](http://localhost:8000/docs) to test the backend API with Swagger UI.

## 🔄 CI/CD and Deployment

- **CI/CD**: GitHub Actions automatically build and deploy backend and frontend upon push to `main`.
- **Render Deployment**:
  - Backend: Deployed as a **Web Service** with Docker.
  - Frontend: Deployed as a **Static Site** with `build` as the output directory.

## 📌 Validation Against Resume & LinkedIn

✅ CI/CD pipeline using GitHub Actions  
✅ Dockerized FastAPI backend and React frontend  
✅ PostgreSQL integration with Alembic migrations  
✅ Render deployment (backend and frontend)  
✅ Functional CRUD app with working endpoints and live demo

## 📞 Credits

This project was built by Siva Ramakrishna Palaparthy as a CI/CD-enabled full-stack portfolio piece to demonstrate end-to-end application design and deployment.

M.S. Computer Science, Syracuse University  
Email: krishpalaparthy6768@gmail.com
