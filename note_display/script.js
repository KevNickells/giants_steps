fetch("first_notes.json")
    .then((r) => r.json())
    .then((data) => {
        data.forEach((datum) => {
            console.log(datum.image);
            console.log(datum.frequency);
        });
    });

const data = [
    { name: "first", duration: 5, value: "Hello" },
    { name: "second", duration: 3, value: "World" },
    { name: "third", duration: 4, value: "This is sequential" },
];

const displayElement = document.getElementById("display");
let currentIndex = 0;
let countdownInterval;

function displayNext() {
    if (currentIndex < data.length) {
        const item = data[currentIndex];
        let timeRemaining = item.duration;

        updateDisplay(item.value, timeRemaining);

        countdownInterval = setInterval(() => {
            timeRemaining--;
            if (timeRemaining >= 0) {
                updateDisplay(item.value, timeRemaining);
            }
        }, 1000);

        setTimeout(() => {
            clearInterval(countdownInterval);
            currentIndex++;
            displayNext();
        }, item.duration * 1000);
    } else {
        displayElement.innerHTML = "Done";
    }
}

function updateDisplay(value, timeRemaining) {
    displayElement.innerHTML = `
        <div class="value">${value}</div>
        &nbsp;
        &nbsp;
        &nbsp;
        <div class="countdown">${timeRemaining}s</div>
    `;
}

displayNext();
