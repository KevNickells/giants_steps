const DURATION = 9;
fetch("_fourth_notes.json")
    .then((r) => r.json())
    .then((data) => {
        const divs = {
            container: document.getElementById("container"),
            currentNote: document.getElementById("currentNote"),
            currentChord: document.getElementById("currentChord"),
            objectFrequency: document.getElementById("objectFrequency"),
            currentFrequency: document.getElementById("currentFrequency"),
            image: document.getElementById("image"),
            remaining: document.getElementById("remaining"),
            next: document.getElementById("next"),
            nextNote: document.getElementById("nextNote"),
        };

        const socket = io("http://localhost:5000");

        socket.on("frequency", function (frequencyData) {
            console.log(frequencyData);
            divs.currentFrequency.textContent =
                frequencyData.frequency.toFixed(1);
        });

        let currentIndex = 0;
        let countdownInterval;

        function displayNext() {
            if (currentIndex < data.length) {
                const item = data[currentIndex];
                let timeRemaining = DURATION;

                const nextImage = data[currentIndex + 1]
                    ? data[currentIndex + 1].image
                    : "";

                updateDisplay(
                    currentIndex,
                    item.full_chord,
                    item.frequency,
                    item.image,
                    nextImage,
                    timeRemaining,
                );

                countdownInterval = setInterval(() => {
                    timeRemaining--;
                    if (timeRemaining >= 0) {
                        updateDisplay(
                            currentIndex,
                            item.full_chord,
                            item.frequency,
                            item.image,
                            nextImage,
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
            currentIndex,
            currentChord,
            frequency,
            image,
            nextImage,
            timeRemaining,
        ) {
            const currentNote = image.replace(/\.png/, "");
            const nextNote = nextImage.replace(/\.png/, "");

            console.log(currentIndex);

            divs.currentChord.textContent = currentChord;
            divs.currentNote.textContent = currentNote;
            divs.objectFrequency.textContent = frequency;
            divs.image.src = `note_images/${image}`;
            divs.remaining.textContent = timeRemaining;
            divs.next.src = `note_images/${nextImage}`;
            divs.nextNote.textContent = nextNote;
        }

        displayNext();
    });
