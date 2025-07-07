require('dotenv').config();
const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');

const app = express();

const BOT_TOKEN = process.env.BOT_TOKEN;
const CHAT_ID = process.env.CHAT_ID;
const PORT = process.env.PORT || 4509;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/submit-challenge', async (req, res) => {
  const {
    name, title, description, point, level,
    flag, hint, tags, category, link
  } = req.body;

  // Validasi dasar
  if (!name || !title || !description || !point || !level || !flag || !category || !link) {
    return res.status(400).json({ success: false, error: 'Semua field wajib diisi.' });
  }

  // Validasi lanjutan
  if (typeof point !== 'number' || point < 1 || point > 1000) {
    return res.status(400).json({ success: false, error: 'Point harus antara 1-1000.' });
  }

  if (!/^https?:\/\/\S+$/i.test(link)) {
    return res.status(400).json({ success: false, error: 'Link tidak valid.' });
  }

  if (!['Easy', 'Medium', 'Hard'].includes(level)) {
    return res.status(400).json({ success: false, error: 'Level harus Easy, Medium, atau Hard.' });
  }

  const message = `
📥 *Kontribusi Soal CTF*
👤 *Nama:* ${name}
🏷️ *Judul:* ${title}
📂 *Kategori:* ${category}
⭐ *Point:* ${point}
🎯 *Level:* ${level}

📝 *Deskripsi:*
${description}

🧠 *Hint:* ${hint || '-'}
🏷️ *Tags:* ${tags || '-'}
🚩 *Flag:* \`${flag}\`
🔗 *Link:* ${link}
`;

  try {
    await axios.post(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
      chat_id: CHAT_ID,
      text: message,
      parse_mode: 'Markdown'
    });
    res.json({ success: true });
  } catch (err) {
    console.error('Telegram Error:', err.response?.data || err.message);
    res.status(500).json({ success: false, error: 'Gagal mengirim ke Telegram.' });
  }
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});

