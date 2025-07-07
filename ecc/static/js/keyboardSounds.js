document.addEventListener('keydown', function (e) {
  const audio = new Audio('/static/sound/keypress.mp3');
  audio.volume = 0.2;
  audio.play();
});

