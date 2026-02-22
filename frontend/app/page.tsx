const cards = [
  { title: 'Admissions', text: 'Explore courses, scholarships and admission process.' },
  { title: 'Student Life', text: 'Clubs, innovation labs, and campus culture.' },
  { title: 'New Initiatives', text: 'AI-first learning and industry aligned curriculum.' },
  { title: 'News & Events', text: 'Stay updated with all latest happenings.' }
];

export default function Home() {
  return (
    <main>
      <section className="bg-gradient-to-r from-primary to-sky-500 py-20 text-white">
        <div className="container-wrap">
          <h1 className="text-4xl font-bold">Unicore AI – Student Login Platform</h1>
          <p className="mt-3 max-w-2xl">Empowering VCSM students with a modern E-Portal for fees, attendance, timetable, exams, events, and placements.</p>
        </div>
      </section>
      <section className="container-wrap -mt-8 grid gap-4 md:grid-cols-4">
        {cards.map((c) => <div key={c.title} className="rounded-xl bg-white p-5 shadow"><h3 className="font-semibold">{c.title}</h3><p className="text-sm text-slate-600">{c.text}</p></div>)}
      </section>
      <section className="container-wrap mt-12 grid gap-6 md:grid-cols-2">
        <div className="rounded-xl bg-white p-6 shadow">
          <h2 className="text-xl font-semibold">Latest News</h2>
          <ul className="mt-4 space-y-3 text-sm">
            <li><b>Jan 05, 2026:</b> VCSM launches AI Innovation Lab. <a className="text-primary" href="/news">See more</a></li>
            <li><b>Jan 01, 2026:</b> Admission portal open for UG programs. <a className="text-primary" href="/news">See more</a></li>
          </ul>
        </div>
        <div className="rounded-xl bg-white p-6 shadow">
          <h2 className="text-xl font-semibold">Useful Links</h2>
          <ul className="mt-4 list-disc space-y-2 pl-5 text-sm">
            <li>Event enrollment</li><li>Downloads</li><li>Academic calendar</li><li>Placement drive registration</li>
          </ul>
        </div>
      </section>
    </main>
  );
}
