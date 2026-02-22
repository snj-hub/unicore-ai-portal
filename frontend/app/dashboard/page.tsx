import Link from 'next/link';

export default function Dashboard() {
  const cards = [
    ['Fees', 'Total ₹21,000 | Paid ₹15,000 | Remaining ₹6,000 (Pending)'],
    ['Attendance', 'Overall 88%'],
    ['Day Order', '3'],
    ['Next Class', '02:40 PM - 03:45 PM AI Lab']
  ];
  return <div className="container-wrap py-10"><h1 className="text-3xl font-bold">Student Dashboard</h1><div className="mt-6 grid gap-4 md:grid-cols-2">{cards.map((c)=> <div key={c[0]} className="rounded-xl bg-white p-5 shadow"><h2 className="font-semibold">{c[0]}</h2><p className="text-sm">{c[1]}</p></div>)}</div><div className="mt-6 flex gap-3">{['fees','attendance','timetable','exams','events','placements','profile'].map((s)=> <Link className="rounded border px-3 py-2 text-sm" key={s} href={`/dashboard/${s}`}>{s}</Link>)}</div></div>;
}
