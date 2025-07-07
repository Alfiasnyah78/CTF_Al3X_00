const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const bird = new Image();
bird.src = "bird.png";

const bg = new Image();
bg.src = "background.png";

const pipeNorth = new Image();
pipeNorth.src = "pipe.png";

const gap = 120;
const constant = pipeNorth.height + gap;

let bX = 50;
let bY = 150;
let gravity = 1.5;
let velocity = 0;
let score = 0;

let pipes = [];
pipes[0] = {
  x: canvas.width,
  y: Math.floor(Math.random() * pipeNorth.height) - pipeNorth.height
};

document.addEventListener("keydown", moveUp);
canvas.addEventListener("click", moveUp);

function moveUp() {
  velocity = -20;
}

function draw() {
  ctx.drawImage(bg, 0, 0);

  for (let i = 0; i < pipes.length; i++) {
    let p = pipes[i];
    ctx.drawImage(pipeNorth, p.x, p.y);
    ctx.drawImage(pipeNorth, p.x, p.y + constant);

    p.x--;

    if (p.x === 125) {
      pipes.push({
        x: canvas.width,
        y: Math.floor(Math.random() * pipeNorth.height) - pipeNorth.height
      });
    }

    if (bX + bird.width >= p.x && bX <= p.x + pipeNorth.width &&
      (bY <= p.y + pipeNorth.height || bY + bird.height >= p.y + constant)) {
      gameOver();
    }

    if (p.x === 5) {
      score++;
    }
  }

  ctx.drawImage(bird, bX, bY);

  velocity += gravity;
  bY += velocity;

  if (bY + bird.height >= canvas.height) {
    gameOver();
  }

  document.getElementById('scoreBoard').innerText = "Score: " + score;

  requestAnimationFrame(draw);
}

function gameOver() {
  document.getElementById('finalScore').value = score;
  alert('Game Over! Your score: ' + score);
  location.reload();
}

draw();

