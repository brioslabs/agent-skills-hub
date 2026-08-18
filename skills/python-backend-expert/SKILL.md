---
name: python-backend-expert
description: >
  Expert guidance for building secure, scalable, and maintainable Python backends using FastAPI, AsyncSQLAlchemy, and Pydantic V2.
  Trigger: When creating, refactoring, or optimizing Python backend architectures, APIs, or database interactions.
license: Apache-2.0
metadata:
  author: brioslabs
  version: "1.0.0"
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

## When to Use

- Building RESTful APIs with FastAPI and Pydantic V2.
- Designing async database access layers using SQLAlchemy 2.0 and AsyncSession.
- Implementing JWT Authentication, Role-Based Access Control (RBAC), and password hashing (Argon2 / bcrypt).
- Configuring Alembic database migrations.
- Structuring modular FastAPI projects using Dependency Injection (`Depends`).

## Critical Patterns

### 1. Strict Typing and Schema Separation
- Always separate Request Schemas (`UserCreate`), Response Schemas (`UserResponse`), and Internal Models (`User`).
- Never leak sensitive fields (passwords, secrets) in response models.

### 2. Async Database Operations
- Never invoke blocking synchronous DB operations inside async path operation functions.
- Always use `AsyncSession` provided via FastAPI dependency injection.

### 3. Error Handling Contract
- Use custom exception classes inheriting from `HTTPException`.
- Return standardized error JSON schemas containing `code`, `message`, and optional `details`.

## Code Examples

### Standard FastAPI Endpoint Pattern

```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

class UserCreateRequest(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        from_attributes = True

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    payload: UserCreateRequest,
    db: AsyncSession = Depends(get_db_session)
):
    # Business logic delegating to service layer
    user = await userService.create_user(db, payload)
    return user
```

## Useful Commands

```bash
# Run dev server with auto-reload
poetry run uvicorn main:app --reload --port 8000

# Run Alembic migrations
poetry run alembic revision --autogenerate -m "migration message"
poetry run alembic upgrade head

# Run tests with pytest
poetry run pytest -v --cov=app
```

## Resources

- **Templates**: See [assets/fastapi_template.py](assets/fastapi_template.py) for complete starter structure.
- **Checklist**: See [references/security_checklist.md](references/security_checklist.md) for backend security rules.
