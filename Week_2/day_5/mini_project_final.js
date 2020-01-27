const MYWORD = 'javascript'

// console.log(MYWORD)

const NumberOf = 10

let WordArray = MYWORD.split('')

// console.log(WordArray)

let DisplayArray = []

for (var i = 0; i < WordArray.length; i++) {
	if(i == 0 || i == WordArray.length-1){
		DisplayArray.push(WordArray[i])
	}
	else {
		DisplayArray.push('*')
	}
}

console.log(DisplayArray)


for (let i = 0; i < NumberOf; i++) {
	let guess = prompt("Let's play hangman. Look at the console for a hint. Guess a letter")
	if (guess.length <= 1){
		for (let j = 0; j < WordArray.length; j++) {
			if (WordArray[j].toLowerCase() == guess.toLowerCase()) {
				DisplayArray[j] = WordArray[j];
			}
		}
		console.log(DisplayArray.join(''))
		if (MYWORD == DisplayArray.join('')) {
			console.log('YOU WON');
			break;
		}
	}
}