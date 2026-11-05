# FastAPI Practice Project

## Project Description
This is a beginner-level REST API project built using Python and FastAPI. The application runs locally and inside Docker.

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- Git

## Requirements
- Python 3.x
- Visual Studio Code
- Git
- Docker Desktop

## Project Setup

### 1. Create and activate virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the API locally

```powershell
uvicorn main:app --reload
```

Open in browser:

- http://localhost:8000
- http://localhost:8000/about
- http://localhost:8000/docs

## Run Using Docker

### 1. Create environment file

```powershell
Copy-Item .env.example .env
```

### 2. Build and start the container

```powershell
docker compose up --build -d
```

### 3. Check container status

```powershell
docker compose ps
```

### 4. Stop the container

```powershell
docker compose down
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home API |
| GET | /about | About project |
| GET | /docs | API documentation |

## Environment Variables

The application uses an `.env` file for local environment configuration.

Do not commit `.env` because it may contain private information.

## Project Status

- FastAPI application created.
- Dependencies installed.
- Dockerfile configured.
- Docker Compose configured.
- Docker container successfully started.
- API tested through the browser.