document.addEventListener('DOMContentLoaded', function () {
  const input = document.getElementById('cmd-input');
  const prompt = document.querySelector('.cmd-prompt');

  if (prompt) {
    prompt.innerText = 'user@retro-ctf:~$ ';
  }

  input.addEventListener('focus', () => {
    document.getElementById('cmd-cursor').style.display = 'inline';
  });

  input.addEventListener('blur', () => {
    document.getElementById('cmd-cursor').style.display = 'none';
  });
});

