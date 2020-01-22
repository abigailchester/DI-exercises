grade = prompt("Enter a grade")

coefficient = prompt("Give a coefficient")

number_of_grades = 3

userGrade = [grade]

userCoefficient = [coefficient]

console.log(userCoefficient)

console.log(coefficient)


if (grade == null && coefficient == null) {
	another_grade = prompt("Enter another grade");
	another_coefficient = prompt("Enter another coefficient");
	console.log((another_grade * another_coefficient)/number_of_grades)
}
else if (grade == null) {
	new_grade = prompt("Enter grade again")
	console.log((new_grade * coefficient)/number_of_grades)
}

else if (coefficient == null) {
	new_coefficient = prompt("Enter coefficient again")
	console.log((grade * new_coefficient)/number_of_grades)
}

else {
	console.log((grade * coefficient)/number_of_grades)
}







