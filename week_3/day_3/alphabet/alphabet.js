const root = document.getElementById("root")

const alphabetlower = "abcdefghijklmnopqrstuvwxyz"

const alphabet = alphabetlower.toUpperCase()

const array = alphabet.split("")

console.log(array)

for (var i = 0; i < array.length; i++) {
	var box = document.createElement("div")
	box.setAttribute("class", "box")
	box.innerText = array[i]
	root.appendChild(box)
	box.style.border = "2px solid black";
	box.style.height = "50px";
	box.style.width = "50px";
	box.style.display = "flex";
	box.style.alignItems = "center";
	box.style.justifyContent = "center";
	// box.style.overflow = "hidden";
	// box.style.position = "fixed"
	// for (var item in box) {
	// 	item.style.position: "absolute" + "50px"
	// }
	// box.style.position = "absolute";
	// box.style.zIndex = "1000";
	// box.style.flexDirection = "row";
	box.setAttribute("draggable", "true");
	box.addEventListener("dragend", function(e){
		let x = e.clientX;
		let y = e.clientY;
		box.style.position = "absolute";
		box.style.left = x + "px";
		box.style.top = y + "px";
		console.log(x, y)

		// box.onmousedown = function(event) {
		// 	box.style.position = "absolute";
		// 	moveAt(event.pageX, event.pageY)
		// }
		// function moveAt(pageX, pageY) {
		// 	box.style.left = pageX - box.offsetWidth / 2 + "px";
		// 	box.style.top = pageY - box.offsetHeight / 2 + "px";
		// }
		function onMouseMove(event){
			moveAt(event.clientX, event.clientY);
		}
		// document.addEventListener("mousemove", onMouseMove);
		// box.onmouseup = function() {
		// 	document.removeEventListener("mousemove", onMouseMove);
		// 	box.onmouseup = null;
		// }
	})

}

//STILL NEED TO DO: 
// 1. align div boxes next to each other - position needs to be absolute except they can't be on top of each other
// 2. make it so that the letter clicked is picked up, rather than Z
// 3. make the position stay even when you pick up another box
