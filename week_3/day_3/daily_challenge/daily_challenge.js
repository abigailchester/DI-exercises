var libButton = document.getElementById('lib-button');
var libIt = function() {
	var storyDiv = document.getElementById("story");
	var noun = document.getElementById("noun")
	var adjective = document.getElementById("adjective")
	var person = document.getElementById("person")
	storyDiv.innerText = "The " + adjective.value + " " + noun.value + " is chasing " + person.value + " away";
};
libButton.addEventListener('click', libIt);
