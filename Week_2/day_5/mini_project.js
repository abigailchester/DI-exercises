secret_word = "crocodile"


// let word2 = prompt("Enter a word:");
// let new_word2 = word2.charAt(0) + Array(word2.length-2).fill("*").join("") + word2.charAt(word2.length -1);
// console.log(new_word2)
let between = Array(secret_word.length-2).fill("*").join("")

let firstLetter = secret_word.charAt(0)

let lastLetter = secret_word.charAt(secret_word.length-1)

let hint = firstLetter + between + lastLetter

let guess1 = prompt("Let's play hangman. Here is your hint \n" + hint + "\n Guess a letter")

let secret_array = secret_word.split("")

console.log(secret_array)

if (secret_array.includes(guess1)) {
//	let new_word = secret_word.charAt(0) +  + secret_word.charAt(secret_word.length-1)
	let new_word = firstLetter + between.replace(/ /, guess1) + lastLetter
		//do if or while loop here, turn to array and back 
	let next_word = prompt("you guessed a letter. guess another letter \n" + new_word)
}



