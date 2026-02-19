const DURATION = 9;
fetch("first_notes.json")
    .then((r) => r.json())
    .then((data) => {
        const socket = io("http://localhost:5000");

        socket.on("frequency", function (data) {
            console.log(data.frequency.toFixed(1));
        });

        const divs = {
            container: document.getElementById("container"),
            currentNote: document.getElementById("currentNote"),
            currentChord: document.getElementById("currentChord"),
            frequency: document.getElementById("frequency"),
            image: document.getElementById("image"),
            remaining: document.getElementById("remaining"),
            next: document.getElementById("next"),
            nextNote: document.getElementById("nextNote"),
        };
        let currentIndex = 0;
        let countdownInterval;

        function displayNext() {
            if (currentIndex < data.length) {
                const item = data[currentIndex];
                let timeRemaining = DURATION;

                updateDisplay(
                    item.full_chord,
                    item.frequency,
                    item.image,
                    data[currentIndex + 1].image,
                    timeRemaining,
                );

                countdownInterval = setInterval(() => {
                    timeRemaining--;
                    if (timeRemaining >= 0) {
                        updateDisplay(
                            item.full_chord,
                            item.frequency,
                            item.image,
                            data[currentIndex + 1].image,
                            timeRemaining,
                        );
                    }
                }, 1000);

                setTimeout(() => {
                    clearInterval(countdownInterval);
                    currentIndex++;
                    displayNext();
                }, DURATION * 1000);
            } else {
                displayElement.innerHTML = "Done";
            }
        }

        function updateDisplay(
            currentChord,
            frequency,
            image,
            nextImage,
            timeRemaining,
        ) {
            const currentNote = image.replace(/\.png/, "");
            const nextNote = nextImage.replace(/\.png/, "");

            divs.currentChord.textContent = currentChord;
            divs.currentNote.textContent = currentNote;
            divs.frequency.textContent = frequency;
            divs.image.src = `note_images/${image}`;
            divs.remaining.textContent = timeRemaining;
            divs.next.src = `note_images/${nextImage}`;
            divs.nextNote.textContent = nextNote;
        }

        displayNext();
    });
