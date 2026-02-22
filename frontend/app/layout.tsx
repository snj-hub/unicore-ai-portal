import './globals.css';
import { SiteShell } from '@/components/site-shell';
import { VcsmBot } from '@/components/vcsm-bot';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <SiteShell>{children}</SiteShell>
        <VcsmBot />
      </body>
    </html>
  );
}
