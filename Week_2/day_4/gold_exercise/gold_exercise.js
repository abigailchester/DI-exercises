function playTheGame() {
	var answer = confirm("Do you want to play the game?")
		if (answer == true) {
			var stringedNumber = prompt("Enter a number between 0 and 10")
			var myNumber = Math.floor(stringedNumber);
			console.log(myNumber)
			if (myNumber < 0 || myNumber > 10) {
				alert("Sorry it's not a good number, Goodbye")
			}
			else if (isNaN(myNumber)) {
				alert("Sorry Not a number, Goodbye")
			}
			else if (myNumber >= 0 && myNumber <= 10) {
				var computerNumber = Math.floor(Math.random() * 10)
				alert(computerNumber)
			}
		}
		else {
			alert("No problem, Goodbye")
		}


// playTheGame()


function test(myNumber, computerNumber) {
	// var myNumber = prompt("Guess a number")
	if (myNumber == computerNumber) {
		alert("You won!")
	}
	else if (myNumber > computerNumber) {
		let secondGuess = prompt("Your number is bigger, guess again")
		if (secondGuess == computerNumber) {
			alert("You won!")
		}
		else {
			let thirdguess = prompt("wrong, guess again")
			if (thirdguess == computerNumber) {
				alert("You won!")
			}
			else {
				alert("You can't try again, the number is " + computerNumber)
			}
		}
	}
	else if (myNumber < computerNumber) {
		let secondGuess = prompt("Your number is smaller, guess again")
		if (secondGuess == computerNumber) {
			alert("You won!")
		}
		else {
			let thirdguess = prompt("wrong, guess again")
			if (thirdguess == computerNumber) {
				alert("You won!")
			}
			else {
				alert("You can't try again, the number is " + computerNumber)
			}
		}
	}
}
test(myNumber, computerNumber)

}






