'use client';

import { useState } from 'react';

export default function EPortal() {
  const [mobile, setMobile] = useState('');
  const [otp, setOtp] = useState('');
  return (
    <div className="container-wrap py-12">
      <h1 className="text-3xl font-bold">E-Portal Login</h1>
      <div className="mt-6 max-w-md space-y-3 rounded-xl bg-white p-6 shadow">
        <input className="w-full rounded border p-2" value={mobile} onChange={(e) => setMobile(e.target.value)} placeholder="Mobile number" />
        <button className="w-full rounded bg-primary p-2 text-white">Request OTP</button>
        <input className="w-full rounded border p-2" value={otp} onChange={(e) => setOtp(e.target.value)} placeholder="Enter OTP" />
        <button className="w-full rounded bg-accent p-2 text-white">Verify OTP</button>
        <button className="w-full rounded border p-2">Continue with Google (@vcsm.ac.in only)</button>
      </div>
    </div>
  );
}
