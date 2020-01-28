var email_input = document.createElement("input")

var submit_button = document.createElement("button")
submit_button.innerText = "Submit email"

email_input.setAttribute("type", "text");
email_input.setAttribute("placeholder", "enter your email")
email_input.setAttribute("id", "emailinput")

submit_button.addEventListener("click", function(e){
	let forminput = document.getElementById("emailinput");
	// console.log(forminput.value)
	let x = forminput.value
	console.log(x)
	function validate(x){
		if (x.includes("@") && x.includes(".com")) {
			alert("thank you!")
		}
		else {
			alert("invalid email")
		}
	}
	validate(x)
})


var root = document.getElementById("root")
root.appendChild(email_input)
root.appendChild(submit_button)

