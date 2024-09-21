function updateClock() {
    fetch('/time')
        .then(response => response.text())
        .then(time => {
            document.getElementById('clock').textContent = time;
        });
}

document.addEventListener('DOMContentLoaded', () => {
    setInterval(updateClock, 1000);
});