// server.js
const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'dist')));

const FLAG = 'CTF{you_triggered_xss_successfully}';

app.get('/flag', (req, res) => {
  const ua = req.headers['user-agent'];
  if (ua.includes('Mozilla')) {
    res.send(`<h3>🎉 Flag: ${FLAG}</h3>`);
  } else {
    res.status(403).send('Forbidden');
  }
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

app.listen(8567, () => {
  console.log('Server running on http://localhost:8567');
});

