import { DashboardLayout } from '@/components/dashboard-layout';

export default function FeesPage() {
  const total = 21000; const paid = 15000; const rem = total - paid;
  return <DashboardLayout title="Fees Status"><div className="grid gap-3 md:grid-cols-3"><Card k="Total" v={`₹${total}`} /><Card k="Paid" v={`₹${paid}`} cls="text-green-600" /><Card k="Remaining" v={`₹${rem} ${rem===0?'Paid':'Pending'}`} cls={rem===0?'text-green-600':'text-red-600'} /></div></DashboardLayout>;
}
function Card({k,v,cls=''}:{k:string;v:string;cls?:string}){return <div className="rounded border p-3"><p className="text-xs text-slate-500">{k}</p><p className={`font-semibold ${cls}`}>{v}</p></div>;}
