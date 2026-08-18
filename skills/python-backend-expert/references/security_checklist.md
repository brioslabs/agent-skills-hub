# Backend Security Checklist (brioslabs)

- [ ] **Authentication**: Use JWT tokens signed with HS256/RS256 and expiration set (e.g. 15-30 min access token, 7d refresh token).
- [ ] **Password Hashing**: Store passwords hashed with `passlib[argon2]` or `bcrypt`.
- [ ] **Input Validation**: Enforce strict length, regex, and type rules via Pydantic models.
- [ ] **CORS Settings**: Do not use `allow_origins=["*"]` in production. Limit to trusted domains.
- [ ] **Database Injection Protection**: Always use ORM parameter binding (SQLAlchemy) or parameterized raw queries.
- [ ] **Environment Variables**: Store API keys, DB passwords, and secrets in `.env` or secret manager (never hardcoded in git).
- [ ] **Rate Limiting**: Apply rate limiting middleware on public routes (e.g., login, register).
