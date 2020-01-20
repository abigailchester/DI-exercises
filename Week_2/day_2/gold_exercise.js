//	Exercise 1

var num = prompt("Enter number here")


if (num % 2 == 0) {
	console.log(num + " is an even number")
}

else {
	console.log(num + " is not an even number")
}


//Exercise 2


var x = 10
var y = 9

if (x > y) {
	console.log(x)
}

else {
	console.log(y)
}


// Exercise 3

var language = prompt("What language do you speak?")

if (language == "French") {
	console.log("Bonjour")
}

else if (language == "English") {
	console.log("Hello")
}

else if (language == "Hebrew") {
	console.log("Shalom")
}

else {
	console.log("😊")
}


// Exercise 4

var grade = prompt("Enter your grade")


if (grade > 90) {
	console.log("A")
}
else if (grade > 80 && grade < 90) {
	console.log("B")
}
else if (grade > 70 && grade < 80) {
	console.log("C")
}
else {
	console.log("D")
}