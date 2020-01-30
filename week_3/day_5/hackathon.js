//add buttons so they can touch an instrument and play it themselves


buttons = document.getElementsByClassName("btn btn-primary")

console.log(buttons)

// for (button of buttons){
// 	button.addEventListener("click", function(e){
// 		alert("lyrics")
// 	})
// }


// button1 = document.getElementById("button1")

// button1.addEventListener("click", function(e){
// 	alert("lyrics to baby shark")
// })

// button2 = document.getElementById("button2")

// button2.addEventListener("click", function(e){
// 	alert("lyrics to twinkle twinkle")
// })

// button3 = document.getElementById("button3")

// button3.addEventListener("click", function(e){
// 	alert("lyrics to mary had a little lamb")
// })

// button4 = document.getElementById("button4")

// button4.addEventListener("click", function(e){
// 	alert("lyrics to old mcdonald")
// })

// button5 = document.getElementById("button5")

// button5.addEventListener("click", function(e){
// 	alert("lyrics to itsy bitsy spider")
// })

// button6 = document.getElementById("button6")

// button6.addEventListener("click", function(e){
// 	alert("lyrics to alphabet")
// })

// button7 = document.getElementById("button7")

// button7.addEventListener("click", function(e){
// 	alert("lyrics to if you're happy and you know it")
// })

// button8 = document.getElementById("button8")

// button8.addEventListener("click", function(e){
// 	alert("lyrics to wheels on the bus")
// })

// button9 = document.getElementById("button9")

// button9.addEventListener("click", function(e){
// 	alert("lyrics to 5 little ducks")
// })


function showtext() {  
    var dialog2 = document.getElementById('dialog2');  
    document.getElementById('show2').onclick = function() {  
        dialog2.show();  
    };  
    document.getElementById('hide2').onclick = function() {  
        dialog2.close();  
    };  
}
showtext(); 

console.log(document.getElementsByClassName("card")[2])

var cards = document.getElementsByClassName("card")

// for (i = 0; i < cards.length; i++) {
// 	var card = document.getElementsByClassName("card")[i]
// 	//then get element by child nodes, do each thing to button etc
// }

// for (i = 0; i < cards.length; i++) {
// 	var 
// }
console.log(document.getElementsByClassName("showbutton")[2])

