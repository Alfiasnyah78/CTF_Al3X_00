import React, { useState, useEffect } from "react";
import XSSChallenge from './XSSChallenge';

const days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"];

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6">🛡️ Study Scheduler + XSS Lab</h1>
      <XSSChallenge />
    </div>
  );

export default function App() {
  const [schedule, setSchedule] = useState(() => {
    const stored = localStorage.getItem("studySchedule");
    return stored ? JSON.parse(stored) : {};
  });
  const [day, setDay] = useState("Senin");
  const [time, setTime] = useState("");

  useEffect(() => {
    localStorage.setItem("studySchedule", JSON.stringify(schedule));
  }, [schedule]);

  const addTimeSlot = () => {
    if (!time) return;
    setSchedule((prev) => ({
      ...prev,
      [day]: prev[day] ? [...prev[day], time] : [time],
    }));
    setTime("");
  };

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">Jadwal Belajar Mingguan</h1>
      <div className="flex gap-2 items-center mb-4">
        <select
          className="border rounded p-2"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        >
          {days.map((d) => (
            <option key={d} value={d}>
              {d}
            </option>
          ))}
        </select>
        <input
          className="border rounded p-2 flex-grow"
          placeholder="Contoh: 19:00 - 20:00"
          value={time}
          onChange={(e) => setTime(e.target.value)}
        />
        <button onClick={addTimeSlot} className="bg-blue-600 text-white px-4 py-2 rounded">
          Tambah
        </button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {days.map((d) => (
          <div key={d} className="bg-white rounded shadow p-4">
            <h2 className="text-xl font-semibold mb-2">{d}</h2>
            <ul className="list-disc list-inside space-y-1">
              {(schedule[d] || []).map((t, i) => (
                <li key={i}>{t}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
