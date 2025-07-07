const commandInput = document.getElementById('commandInput');
const output = document.getElementById('output');

const commands = {
    'help': 'Available commands: about, skills, experience, contact, clear',
    'about': 'Nama saya Ahmad. Saya bergerak di bidang Cyber Security dan Ethical Hacking.',
    'skills': 'Web Security, System Administration',
    'experience': 'Pengalaman: Cyber Security',
    'contact': 'Email: lol@gmail.com | LinkedIn: linkedin.com/in/ahmad',
};

commandInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        const input = commandInput.value.trim();
        if (input === 'clear') {
            output.innerHTML = '';
        } else {
            const response = commands[input] || `Command not found: ${input}`;
            output.innerHTML += `<div><span class="prompt">ahmad@kali:~$</span> ${input}</div>`;
            output.innerHTML += `<div>${response}</div>`;
        }
        commandInput.value = '';
        window.scrollTo(0, document.body.scrollHeight);
    }
});
