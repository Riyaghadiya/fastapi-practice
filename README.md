# FastAPI Practice Project

## Project Description
This is a beginner-level REST API project built using Python and FastAPI. It provides CRUD operations to manage users.

## Technologies Used
- Python
- FastAPI
- Uvicorn
- Pydantic
- Postman
- Git and GitHub
- Docker and Docker Compose

## Requirements
- Python 3.x
- Visual Studio Code
- Git
- Postman
- Docker Desktop (optional)

## Project Structure

```text
fastapi-practice/
├── main.py
├── routers/
│   └── users.py
├── schemas/
│   └── user.py
├── services/
│   └── user_service.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Project Setup

### 1. Create a virtual environment

```powershell
python -m venv venv
```

### 2. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Start the API locally

```powershell
uvicorn main:app --reload
```

The API will run at:

http://127.0.0.1:8000

Open API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home |
| GET | /health | Health check |
| GET | /about | Project information |
| POST | /users/ | Create user |
| GET | /users/ | Get all users |
| GET | /users/{user_id} | Get user by ID |
| PUT | /users/{user_id} | Update user |
| DELETE | /users/{user_id} | Delete user |

## Testing

All user CRUD endpoints can be tested using Postman.

Example user JSON:

```json
{
  "name": "Riya",
  "email": "riya@example.com",
  "phone": "9876543210",
  "status": "active"
}
```

## Git Workflow

Initialize Git:

```powershell
git init
```

Create a feature branch:

```powershell
git switch -c feature/user-crud
```

Add and commit files:

```powershell
git add .
git commit -m "Initial FastAPI project setup"
```

Connect GitHub repository:

```powershell
git remote add origin https://github.com/Riyaghadiya/fastapi-practice.git
```

Push code:

```powershell
git push -u origin main
```

## Important Note

The current user data is stored in an in-memory dictionary. Data will be lost when the API restarts.

Never upload the `.env` file or private credentials to GitHub. Use `.env.example` as a template.

## Project Status

- FastAPI application created.
- CRUD operations implemented.
- API tested using Postman.
- Git repository initialized.
- GitHub repository connected.
- Project uploaded to GitHub.