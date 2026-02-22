import Link from 'next/link';

const links = ['fees','attendance','timetable','exams','events','placements','profile'];

export function DashboardLayout({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="container-wrap py-10">
      <h1 className="text-3xl font-bold">{title}</h1>
      <div className="mt-4 grid gap-6 md:grid-cols-[220px_1fr]">
        <aside className="rounded-xl bg-white p-4 shadow">
          <nav className="space-y-2 text-sm">{links.map((l) => <Link key={l} className="block capitalize hover:text-primary" href={`/dashboard/${l}`}>{l}</Link>)}</nav>
        </aside>
        <section className="rounded-xl bg-white p-6 shadow">{children}</section>
      </div>
    </div>
  );
}
