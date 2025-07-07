// src/XSSChallenge.jsx
import { useState } from 'react';

export default function XSSChallenge() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');

  return (
    <div className="p-6 bg-white rounded shadow max-w-xl mx-auto mt-8">
      <h2 className="text-xl font-bold mb-4">💥 XSS Challenge</h2>
      <p className="mb-2">Masukkan komentar kamu (coba XSS):</p>
      <textarea
        className="w-full p-2 border border-gray-300 rounded mb-4"
        rows="4"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={() => setOutput(input)}
      >
        Submit
      </button>

      <h3 className="text-lg font-semibold mt-6 mb-2">Output:</h3>
      <div className="p-4 border bg-gray-50" dangerouslySetInnerHTML={{ __html: output }} />
    </div>
  );
}

