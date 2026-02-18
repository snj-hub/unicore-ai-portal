from datetime import datetime, time


WEEKDAY_TIMETABLE = [
    {"period": 1, "start": time(9, 0), "end": time(9, 50), "subject": "Data Structures"},
    {"period": 2, "start": time(9, 50), "end": time(10, 40), "subject": "DBMS"},
    {"period": 3, "start": time(10, 55), "end": time(11, 45), "subject": "Python Lab"},
    {"period": 4, "start": time(11, 45), "end": time(12, 35), "subject": "Operating Systems"},
    {"period": 5, "start": time(13, 20), "end": time(14, 10), "subject": "Computer Networks"},
    {"period": 6, "start": time(14, 10), "end": time(15, 0), "subject": "Project Work"},
]

DAY_ORDER_BY_WEEKDAY = {
    0: "Day Order 1 (Monday)",
    1: "Day Order 2 (Tuesday)",
    2: "Day Order 3 (Wednesday)",
    3: "Day Order 4 (Thursday)",
    4: "Day Order 5 (Friday)",
    5: "Holiday Schedule (Saturday)",
    6: "Holiday (Sunday)",
}


class VCSMBotService:
    @staticmethod
    def _greeting_by_time(now: datetime) -> str:
        if now.hour < 12:
            return "Good morning"
        if now.hour < 17:
            return "Good afternoon"
        return "Good evening"

    @staticmethod
    def _current_period(now: datetime):
        current_time = now.time()
        for slot in WEEKDAY_TIMETABLE:
            if slot["start"] <= current_time < slot["end"]:
                return slot
        return None

    @staticmethod
    def _next_period(now: datetime):
        current_time = now.time()
        for slot in WEEKDAY_TIMETABLE:
            if current_time < slot["start"]:
                return slot
        return None

    @staticmethod
    def get_reply(user_message: str) -> str:
        now = datetime.now()
        message = user_message.lower().strip()

        if message in {"hi", "hello", "hey", "good morning", "good evening"}:
            greeting = VCSMBotService._greeting_by_time(now)
            return f"{greeting}! I am VCSM Bot 👋. Ask me about timetable, day order, or current period."

        if "day order" in message:
            return f"Today is {DAY_ORDER_BY_WEEKDAY[now.weekday()]}."

        if "today" in message and "timetable" in message:
            rows = [
                f"P{slot['period']}: {slot['subject']} ({slot['start'].strftime('%I:%M %p')} - {slot['end'].strftime('%I:%M %p')})"
                for slot in WEEKDAY_TIMETABLE
            ]
            return "Here is today's timetable:\n" + "\n".join(rows)

        if "which period" in message or "period is now" in message:
            current = VCSMBotService._current_period(now)
            if not current:
                return "No class is running right now."
            remaining = datetime.combine(now.date(), current["end"]) - now
            minutes_left = int(remaining.total_seconds() // 60)
            return (
                f"You are currently in Period {current['period']} ({current['subject']}). "
                f"It ends at {current['end'].strftime('%I:%M %p')} with {minutes_left} minutes remaining."
            )

        if "next period" in message or "when does the next period start" in message:
            next_slot = VCSMBotService._next_period(now)
            if not next_slot:
                return "There are no more classes for today."
            return (
                f"Next is Period {next_slot['period']} ({next_slot['subject']}) starting at "
                f"{next_slot['start'].strftime('%I:%M %p')}."
            )

        if "start time" in message or "end time" in message:
            first = WEEKDAY_TIMETABLE[0]["start"].strftime("%I:%M %p")
            last = WEEKDAY_TIMETABLE[-1]["end"].strftime("%I:%M %p")
            return f"Classes start at {first} and end at {last}."

        return (
            "I can help with timetable, day order, current period, next period, and class timings. "
            "Try asking: 'What is today's timetable?'"
        )
