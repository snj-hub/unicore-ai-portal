'use client';

import { MessageCircle, Send } from 'lucide-react';
import { useMemo, useState } from 'react';
import { formatTime, greetingForNow } from '@/lib/utils';

type Msg = { from: 'bot' | 'user'; text: string };

export function VcsmBot({ loggedIn = false }: { loggedIn?: boolean }) {
  const [open, setOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Msg[]>([{ from: 'bot', text: `${greetingForNow()}! I am VCSM Bot. Ask timetable, day order, exams, events, fees, placements.` }]);

  const reply = useMemo(() => (q: string) => {
    const question = q.toLowerCase();
    if (question.includes('today timetable') || question.includes('next class')) {
      return `Today classes: 09:00 AM - 09:50 AM Mathematics, 10:00 AM - 10:50 AM Physics. Next class: 02:40 PM - 03:45 PM AI Lab.`;
    }
    if (question.includes('day order')) return 'Today is Day Order 3.';
    if (question.includes('fees')) return loggedIn ? 'Fees status: Total ₹21,000, Paid ₹15,000, Remaining ₹6,000 (Pending).' : 'Please login to E-Portal to view your personal fees status.';
    if (question.includes('exam')) return 'Upcoming exam: Data Structures on 2026-03-02 at 10:00 AM.';
    if (question.includes('event')) return 'Upcoming event: Innovation Summit on 2026-03-05.';
    if (question.includes('placement')) return 'Placement highlights: 78% placed, top package ₹12 LPA.';
    return 'I can help with timetable, day order, fees, exams, events, and placements. Which one would you like?';
  }, [loggedIn]);

  return (
    <div className="fixed bottom-4 right-4 z-50">
      {open && (
        <div className="mb-3 w-80 rounded-2xl border bg-white p-3 shadow-2xl">
          <div className="max-h-80 space-y-2 overflow-auto text-sm">
            {messages.map((m, i) => <p key={i} className={m.from === 'bot' ? 'text-slate-800' : 'text-right text-primary'}>{m.text}</p>)}
          </div>
          <div className="mt-2 flex gap-2">
            <input value={input} onChange={(e) => setInput(e.target.value)} className="flex-1 rounded border p-2 text-sm" placeholder="Ask VCSM Bot..." />
            <button onClick={() => {
              if (!input.trim()) return;
              setMessages((prev) => [...prev, { from: 'user', text: input }, { from: 'bot', text: reply(input) }]);
              setInput('');
            }} className="rounded bg-primary px-3 text-white"><Send className="h-4 w-4" /></button>
          </div>
        </div>
      )}
      <button onClick={() => setOpen((v) => !v)} className="rounded-full bg-primary p-4 text-white shadow-xl"><MessageCircle /></button>
    </div>
  );
}
