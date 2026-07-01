const passwordInput = document.getElementById('password');
const toggleBtn = document.getElementById('toggle-btn');
const strengthMeter = document.getElementById('strength-meter');
const feedbackText = document.getElementById('feedback-text');

toggleBtn.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = 'Hide';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = 'Show';
    }
});

passwordInput.addEventListener('input', async () => {
    const val = passwordInput.value;
    if (!val) {
        strengthMeter.className = 'meter-bar';
        feedbackText.textContent = 'Enter a password to check its strength.';
        return;
    }

    const res = await fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password: val })
    });
    const data = await res.json();

    strengthMeter.className = `meter-bar ${data.strength}`;
    feedbackText.textContent = `Password Security Level: ${data.strength.toUpperCase()}`;
});