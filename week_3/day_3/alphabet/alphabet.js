const root = document.getElementById("root")
root.style.display = "flex"
root.style.width = "100%"
root.style.alignItems = "flex-start"


const alphabetlower = "abcdefghijklmnopqrstuvwxyz"

const alphabet = alphabetlower.toUpperCase()

const array = alphabet.split("")

console.log(array)


for (var i = 0; i < array.length; i++) {
	var box = document.createElement("div")
	box.setAttribute("class", "box")
	box.innerText = array[i]
	box.style.border = "2px solid black";
	box.style.height = "50px";
	box.style.width = "50px";
	box.style.display = "flex";
	box.style.alignItems = "center";
	box.style.justifyContent = "center";
	box.setAttribute("draggable", "true");
	root.appendChild(box)
	

	box.addEventListener("dragend", function(e){
		console.log(e.target.innerHTML)
		let x = e.clientX;
		let y = e.clientY;
		e.target.style.left = x + "px";
		e.target.style.top = y + "px";
		e.target.style.position= "absolute"
		console.log(x, e.target.style.left)

	})

}