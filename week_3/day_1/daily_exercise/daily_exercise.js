var book1 = {
	title: "The Hunger Games",
	author: "Suzanne Collins",
	image_url: "Insert image URL here",
	already_read: true,
}

var book2 = {
	title: "The Glass Castle",
	author: "Jeannette Walls",
	image_url: "Insert image URL here",
	already_read: true,
}

var book3 = {
	title: "To Kill A Mockingbird",
	author: "Harper Lee",
	image_url: "insert image URL here",
	already_read: false,
}

var allBooks = [book1, book2, book3]

console.log(allBooks)


let table = document.createElement("div")


console.log(table)

table.setAttribute("class", "table")
table.id = "contents"




console.log(table.children)

let text = document.createTextNode("this title is written by this author")

console.log(text)

let display = document.createElement("p")

display.appendChild(text)

console.log(display)




for (var y = 0; y < allBooks.length; y++) {
	var finalbooks = allBooks[y].title + " is written by " + allBooks[y].author + allBooks[y].image_url + allBooks[y].already_read + "\n"
	var temp = document.createElement("p")
	// temp[y].id = 'abc-' + y;
	temp.className = "paragraph"
	// temp.className = list
	temp.innerText = finalbooks
	table.appendChild(temp);
	document.write(finalbooks)
}

console.log(table);

// document.write("table3");images

