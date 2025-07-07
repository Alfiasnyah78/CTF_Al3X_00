const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');

const app = express();
require('dotenv').config();

const BOT_TOKEN = process.env.BOT_TOKEN;
const CHAT_ID = process.env.CHAT_ID;

app.use(cors());
app.use(express.json());

// Serve file static dari folder public
app.use(express.static(path.join(__dirname, 'public')));

app.post('/report-bug', async (req, res) => {
  const { name, bug } = req.body;
  const message = `🐞 Bug Report\n👤 Nama: ${name}\n📝 Bug: ${bug}`;
  try {
    await axios.post(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
      chat_id: CHAT_ID,
      text: message
    });
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: 'Gagal kirim ke Telegram' });
  }
});

// Redirect GET / ke index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`✅ Server running on http://localhost:${PORT}`));

