'use client';

import Link from 'next/link';
import { ChevronDown, Menu } from 'lucide-react';
import { useState } from 'react';

const menus = [
  { name: 'About', href: '/about' },
  { name: 'Admissions', href: '/courses-fees' },
  { name: 'Student Life', href: '/events' },
  { name: 'Alumni', href: '/news' },
  { name: 'News & Events', href: '/news' },
  { name: 'Contact', href: '/contact' },
  { name: 'E-Portal', href: '/e-portal' }
];

export function SiteShell({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="min-h-screen">
      <div className="bg-primary text-white">
        <div className="container-wrap flex items-center justify-between py-2 text-sm">
          <span>Valluvar College of Science and Management</span>
          <div className="flex gap-4">
            <Link href="/e-portal">E-Portal</Link>
            <a href="mailto:help@vcsm.ac.in">College Mail</a>
            <Link href="/contact">Contact</Link>
          </div>
        </div>
      </div>
      <header className="bg-white shadow-sm">
        <div className="container-wrap flex items-center justify-between py-4">
          <Link href="/" className="text-xl font-bold text-primary">Unicore AI – Student Login Platform</Link>
          <button className="md:hidden" onClick={() => setOpen((v) => !v)}><Menu /></button>
          <nav className="hidden items-center gap-6 md:flex">
            {menus.map((menu) => (
              <Link key={menu.name} className="group flex items-center gap-1 font-medium hover:text-primary" href={menu.href}>
                {menu.name} {menu.name !== 'E-Portal' && <ChevronDown className="h-4 w-4 opacity-60" />}
              </Link>
            ))}
          </nav>
        </div>
        {open && (
          <nav className="container-wrap grid gap-2 pb-4 md:hidden">
            {menus.map((menu) => <Link key={menu.name} href={menu.href}>{menu.name}</Link>)}
          </nav>
        )}
      </header>
      {children}
      <footer className="mt-16 bg-slate-900 py-10 text-slate-200">
        <div className="container-wrap grid gap-6 md:grid-cols-3">
          <div><h3 className="font-semibold">VCSM</h3><p>123 College Road, Tamil Nadu</p></div>
          <div><h3 className="font-semibold">Quick Links</h3><p>Admissions · Events · Placements · E-Portal</p></div>
          <div><h3 className="font-semibold">Contact</h3><p>+91 9876543210 · info@vcsm.ac.in</p></div>
        </div>
      </footer>
    </div>
  );
}
