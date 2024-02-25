function generateAndColorNumber() {
  let randomNumber = Math.floor(Math.random() * 100) + 1; // Generate random number between 1 and 100
  let randomNumberElement = document.getElementById("random-number");
  randomNumberElement.textContent = "Random Number: " + randomNumber;
  randomNumberElement.style.color = getRandomColor();
}

function getRandomColor() {
  let letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
