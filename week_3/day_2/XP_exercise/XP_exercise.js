let article_array = document.getElementsByTagName("article")

console.log(article_array)

var body_children = document.body.childNodes;

console.log(body_children)


var array = document.getElementsByTagName("p")

array.className = "para_article"

console.log(array)

let paragraphs = document.getElementsByTagName("p");

for (paragraph of paragraphs){
	paragraph.style.color = "blue"

}


paragraphs[array.length - 1].remove()
