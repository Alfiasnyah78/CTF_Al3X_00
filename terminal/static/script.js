const input = document.getElementById("cmdInput");
const outputDiv = document.getElementById("output");
const prompt = document.getElementById("prompt");

let history = [];
let historyIndex = -1;

function updatePrompt(user, host, cwd) {
    const dir = cwd.replace(/^.*[\\/]/, '');
    prompt.textContent = `${user}@${host}:${cwd}$`;
}

input.addEventListener("keydown", async function (e) {
    if (e.key === "Enter") {
        const command = input.value.trim();
        if (!command) return;
        history.push(command);
        historyIndex = history.length;

        outputDiv.innerHTML += `<div><span class="prompt">${prompt.textContent}</span> ${command}</div>`;
        input.value = "";

        if (command === "clear") {
            outputDiv.innerHTML = "";
            return;
        }

        const res = await fetch("/run", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ command })
        });
        const data = await res.json();
        if (data.output) {
            outputDiv.innerHTML += `<pre>${escapeHtml(data.output)}</pre>`;
        }
        if (data.cwd) {
            updatePrompt(data.user, data.host, data.cwd);
        }
        outputDiv.scrollTop = outputDiv.scrollHeight;
    } else if (e.key === "ArrowUp") {
        if (historyIndex > 0) {
            historyIndex--;
            input.value = history[historyIndex];
        }
    } else if (e.key === "ArrowDown") {
        if (historyIndex < history.length - 1) {
            historyIndex++;
            input.value = history[historyIndex];
        } else {
            input.value = "";
        }
    }
});

function escapeHtml(unsafe) {
    return unsafe.replace(/[&<"']/g, function (m) {
        return ({
            '&': '&amp;', '<': '&lt;', '"': '&quot;', "'": '&#039;'
        })[m];
    });
}

