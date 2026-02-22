# Unicore AI – Student Login Platform (VCSM)

Production-ready full-stack app with a premium public college website and secure student E-Portal.

## Stack
- Frontend: Next.js App Router + TypeScript + TailwindCSS + lucide icons + shadcn-style component patterns
- Backend: Flask REST API
- DB: MySQL
- Auth: Mobile OTP + college-domain Google style endpoint
- Bot: in-app VCSM Bot widget with curated intents and safe fallback

## Project Structure
- `frontend/` Next.js app
- `backend/` Flask API
- `backend/sql/schema.sql` DB schema
- `backend/sql/seed.sql` seed data for demo
- `.env.example` environment variables

## Key Features
- Public site routes: `/`, `/about`, `/courses-fees`, `/events`, `/news`, `/placements`, `/contact`, `/e-portal`
- Student routes: `/dashboard`, `/dashboard/fees`, `/dashboard/attendance`, `/dashboard/timetable`, `/dashboard/exams`, `/dashboard/events`, `/dashboard/placements`, `/dashboard/profile`
- Fee status with paid/pending logic and remaining balance
- Timetable time rendering in 12-hour format `hh:mm AM/PM` (including bot responses)
- College email pattern support: `@vcsm.ac.in` with samples like `23051710500111071@vcsm.ac.in`

## Setup
### 1) Database
```bash
mysql -u root -p < backend/sql/schema.sql
mysql -u root -p < backend/sql/seed.sql
```

### 2) Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
python run.py
```

### 3) Frontend
```bash
cd frontend
npm install
cp ../.env.example .env.local
npm run dev
```

Open `http://localhost:3000`.

## Auth Flow
- `POST /api/auth/request-otp`
- `POST /api/auth/verify-otp`
- `POST /api/auth/google` (validates configured college domain)
- JWT Bearer token secures protected dashboard API endpoints

## APIs
- `GET /api/me`
- `GET /api/dashboard/summary`
- `GET /api/fees`
- `GET /api/attendance`
- `GET /api/timetable/today`
- `GET /api/timetable/week`
- `GET /api/day-order/today`
- `GET /api/exams/upcoming`
- `GET /api/events`
- `GET /api/placements/news`

## Notes
- OTP expires in 5 minutes by default, rate-limited and attempt-limited.
- Store only minimal auth data in OTP log table.
- For production, wire real SMS provider and Google OAuth callback.
