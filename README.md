# TaskFlow API

A RESTful personal task management API with secure JWT authentication, full task lifecycle management, advanced search/filtering, and an integrated AI-powered task assistant.

Built for the Backend Developer Internship technical assessment.

## Features

- **Authentication** — Secure registration and login with bcrypt password hashing and JWT-based stateless sessions
- **Task Management** — Full CRUD operations with strict per-user ownership enforcement
- **Search & Filtering** — Case-insensitive title search, status/priority filters, configurable sorting, and pagination
- **AI Task Assistant** — Automatic priority suggestion, categorization, summarization, and productivity tips via the Google Gemini API
- **Centralized Error Handling** — Consistent, structured error responses across the API
- **Interactive API Docs** — Auto-generated Swagger UI

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI (Python) |
| Database | SQLite via SQLAlchemy ORM |
| Auth | JWT (python-jose), bcrypt (passlib) |
| Validation | Pydantic |
| AI Provider | Google Gemini API |

## Project Structure
taskflow-api/
├── app/
│ ├── core/ # config, database, auth dependencies
│ ├── models/ # SQLAlchemy models (User, Task)
│ ├── schemas/ # Pydantic request/response schemas
│ ├── routers/ # API route handlers
│ ├── services/ # business logic (auth, AI)
│ └── main.py
├── requirements.txt
├── .env.example
├── SCHEMA.md
└── README.md

## Getting Started

### Prerequisites
- Python 3.10+
- A Google Gemini API key ([get one here](https://aistudio.google.com/apikey))

### Installation

```bash
git clone https://github.com/anjalipatwal26-ap/taskflow-api.git
cd taskflow-api

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

### Configuration

Copy the example environment file and fill in your values:

```bash
cp .env.example .env
```

```env
DATABASE_URL=sqlite:///./taskflow.db
JWT_SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
```

### Run

```bash
uvicorn app.main:app --reload
```

The API will be live at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## API Reference

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register` | Register a new user |
| POST | `/api/auth/login` | Log in and receive a JWT |

### Users
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/users/me` | Get the authenticated user's profile |

### Tasks
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/tasks` | Create a task |
| GET | `/api/tasks` | List tasks (see query params below) |
| GET | `/api/tasks/{id}` | Get a single task |
| PUT | `/api/tasks/{id}` | Update a task |
| DELETE | `/api/tasks/{id}` | Delete a task |
| PATCH | `/api/tasks/{id}/complete` | Mark task as completed |
| PATCH | `/api/tasks/{id}/pending` | Mark task as pending |
| POST | `/api/tasks/{id}/ai-analyze` | Get AI-generated task insights |

**Query parameters for `GET /api/tasks`:** `search`, `status`, `priority`, `sort_by`, `order`, `page`, `limit`

All task endpoints require `Authorization: Bearer <token>` and are scoped to the authenticated user.

## Database Schema

See [SCHEMA.md](./SCHEMA.md) for the full entity structure and relationships.

## Security

- Passwords hashed with bcrypt, never stored in plain text
- Stateless JWT authentication with expiration
- Strict object-level authorization — users can only access their own tasks
- All secrets loaded from environment variables, never committed to source control
- Centralized exception handling for consistent error responses

## Author

Anjali Patwal