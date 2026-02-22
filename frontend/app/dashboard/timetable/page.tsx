import { DashboardLayout } from '@/components/dashboard-layout';
import { formatTime } from '@/lib/utils';

const rows = [
  ['1', '10:00:00', '10:50:00', 'Mathematics'],
  ['5', '14:40:00', '15:45:00', 'AI Lab']
];

export default function Timetable(){
  return <DashboardLayout title="Timetable"><table className="w-full text-sm"><thead><tr><th className="text-left">Period</th><th className="text-left">Time</th><th className="text-left">Subject</th></tr></thead><tbody>{rows.map((r)=> <tr key={r[0]}><td>{r[0]}</td><td>{formatTime(r[1])} - {formatTime(r[2])}</td><td>{r[3]}</td></tr>)}</tbody></table></DashboardLayout>;
}
