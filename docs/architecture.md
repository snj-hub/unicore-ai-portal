# UniCore AI Phase-1 Architecture (BCA Viva Friendly)

## 1) Project Folder Structure

```text
unicore-ai-portal/
├── app/
│   ├── __init__.py              # Flask app factory and blueprint registration
│   ├── config.py                # Environment and app configuration
│   ├── routes/
│   │   ├── auth.py              # OTP login and logout routes
│   │   ├── dashboard.py         # Student dashboard route
│   │   └── bot.py               # VCSM bot API endpoint
│   ├── services/
│   │   ├── database.py          # MySQL connection helper
│   │   ├── otp_service.py       # OTP generation/verification logic
│   │   └── bot_service.py       # Rule-based chat logic
│   ├── templates/
│   │   ├── base.html            # Common layout + floating bot widget
│   │   ├── login.html           # OTP request page
│   │   ├── verify_otp.html      # OTP verify page
│   │   └── dashboard.html       # Main student portal page
│   └── static/
│       ├── css/styles.css       # App + bot styles
│       └── js/chatbot.js        # Chat widget behavior
├── database/
│   └── schema.sql               # Tables and relations
├── docs/
│   └── architecture.md          # Explainable architecture for viva
├── run.py                       # Entry point
├── requirements.txt             # Python dependencies
└── .env.example                 # Environment template
```

### Why this structure?
- **Routes** contain request/response flow.
- **Services** contain core business logic (easy whiteboard explanation).
- **Templates + Static** keep frontend clean and separated.
- **Database schema** is versioned and easy for demo setup.

---

## 2) Basic Flask Setup

### Core idea
Use **app factory pattern** with blueprints. This keeps project modular but still simple.

### Request flow
1. Browser sends request.
2. Flask route handles endpoint.
3. Route calls service logic (OTP/Bot).
4. Route returns HTML or JSON.

### Implemented modules
- **Auth Module**: request OTP → verify OTP → login session.
- **Dashboard Module**: protected route with sample student cards.
- **Bot Module**: `/api/bot/message` returns VCSM response JSON.

---

## 3) VCSM Bot Architecture (High-Level)

## A. UI Layer
- Floating button at bottom-right.
- Click opens chatbot panel.
- User message bubbles + bot message bubbles.
- Auto-scroll and simple typing placeholder.

## B. API Layer
- Frontend sends message to `POST /api/bot/message`.
- Flask returns `{ "reply": "..." }`.

## C. Logic Layer (Rule-based, Viva Friendly)
`VCSMBotService` handles:
- Greeting detection (`hi`, `hello`, `hey`) with real-time response.
- Day order lookup by weekday.
- Today's timetable response.
- Current period calculation (based on system time).
- Next period prediction.
- Remaining class time calculation.

## D. Data Layer
- Phase-1 uses hardcoded timetable list in `bot_service.py` for simplicity.
- Future phase can move timetable to MySQL tables.

## E. Future AI Upgrade Path
Keep `get_reply()` as abstraction point.
- Today: rule-based `if/else` logic.
- Future: route can forward to OpenAI / local LLM and still keep same UI/API contract.

---

## Local Run (Phase-1)
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and update values.
4. Create DB using `database/schema.sql`.
5. `python run.py`
6. Open `http://127.0.0.1:5000`

