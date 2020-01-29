function myMove(){
	var elem = document.getElementById("animate");
	var pos = 0;
	let id = setInterval(function(){
		if (pos == 350) {
			clearInterval(id);
		}
		else {
			pos++;
			elem.style.left = pos + "px";
		}
	}, 1);
}

let box = document.createElement("div")
box.setAttribute("id", "box")
box.innerText = "Drag me"
box.style.backgroundColor = "pink"
box.style.height = "50px"
box.style.width = "50px"
box.style.left = "50%"
box.setAttribute("draggable", true)

let body = document.getElementsByTagName("body")[0]

body.appendChild(box)

box.addEventListener("dragend", function(e){
	let x = e.clientX;
	let y = e.clientY;
	e.target.style.left = x + "px";
	e.target.style.top = y + "px";
	e.target.style.position= "absolute"
	console.log(x, y)
})