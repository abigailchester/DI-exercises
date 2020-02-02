function showtextShark() {  
    var dialog2 = document.getElementById('dialog2');  
    var babysharklyric = document.createElement("p")
	babysharklyric.setAttribute("class", "lyricscroll")
	babysharklyric.setAttribute("id", "BStext")
    document.getElementById('show2').onclick = function() {  
        dialog2.show();  
        babysharklyric.innerText = "Baby shark, doo doo doo doo doo doo, Baby shark, doo doo doo doo doo doo, Baby shark, doo doo doo doo doo doo, Baby shark!, Mama shark, doo doo doo doo doo doo, Mama shark, doo doo doo doo doo doo, Mama shark, doo doo doo doo doo doo, Mama shark!, Papa shark, doo doo doo doo doo doo, Papa shark, doo doo doo doo doo doo, Papa shark, doo doo doo doo doo doo, Papa shark!, Grandma shark, doo doo doo doo doo doo, Grandma shark, doo doo doo doo doo doo, Grandma shark, doo doo doo doo doo doo, Grandma shark! Grandpa shark, doo doo doo doo doo doo, Grandpa shark, doo doo doo doo doo doo, Grandpa shark, doo doo doo doo doo doo, Grandpa shark! Let's swim faster, doo doo doo doo doo doo, Let's swim faster, doo doo doo doo doo doo, Let's swim faster, doo doo doo doo doo doo, Let's swim faster! Home at last, doo doo doo doo doo doo, Home at last, doo doo doo doo doo doo, Home at last, doo doo doo doo doo doo, Home at last! Baby shark, doo doo doo doo doo doo, Mama shark, doo doo doo doo doo doo, Papa shark, doo doo doo doo doo doo, Grandma shark, doo doo doo doo doo doo, Grandpa shark!, Happy shark, doo doo doo doo doo doo, Happy shark, doo doo doo doo doo doo, Happy shark, doo doo doo doo doo doo, Happy sharks, Happy sharks!"
        dialog2.appendChild(babysharklyric)
    };  
    document.getElementById('hide2').onclick = function() {  
        dialog2.close();  
        dialog2.removeChild(babysharklyric)
    };  
}
showtextShark(); 


function showtextTwinkle() {  
    var dialog4 = document.getElementById('dialog4');  
    var twinkleLyric = document.createElement("p")
	twinkleLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show4').onclick = function() {  
        dialog4.show();  
        twinkleLyric.innerText = "Twinkle, twinkle, little star, How I wonder what you are, Up above the world so high, Like a diamond in the sky, Twinkle, twinkle little star, How I wonder what you are, Twinkle, twinkle, little star, How I wonder what you are, Up above the world so high, Like a diamond in the sky, Twinkle, twinkle little star, How I wonder what you are";
        dialog4.appendChild(twinkleLyric);
    };  
    document.getElementById('hide4').onclick = function() {  
        dialog4.close();  
        dialog4.removeChild(twinkleLyric);
    };  
}
showtextTwinkle(); 

function showtextMary() {  
    var dialog5 = document.getElementById('dialog5');  
    var maryLyric = document.createElement("p")
	maryLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show5').onclick = function() {  
        dialog5.show();  
        maryLyric.innerText = "Mary had a little lamb, Little lamb, little lamb, Mary had a little lamb, Its fleece was white as snow, And everywhere that Mary went, Mary went, Mary went, Everywhere that Mary went, The lamb was sure to go, He followed her to school one day, School one day, school one day, He followed her to school one day, Which was against the rules, It made the children laugh and play, Laugh and play, laugh and play, It made the children laugh and play, To see a lamb at school, And so the teacher turned it out, Turned it out, turned it out, And so the teacher turned it out, But still it lingered near, Why does the lamb love Mary so, Love Mary so, Love Mary so, The eager children cry, Why Mary loves the lamb you know, lamb you know, lamb you know, Why Mary loves the lamb you know, The teacher did reply, Mary had a little lamb, Little lamb, little lamb, Mary had a little lamb, Its fleece was white as snow"
        dialog5.appendChild(maryLyric);
    };  
    document.getElementById('hide5').onclick = function() {  
        dialog5.close();  
        dialog5.removeChild(maryLyric);
    };  
}
showtextMary(); 


function showtextOldmac() {
    var dialog6 = document.getElementById('dialog6');
    var oldmacLyric = document.createElement("p")
	oldmacLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show6').onclick = function() {
        dialog6.show();
        oldmacLyric.innerText = "Old MACDONALD had a farm, E-I-E-I-O, And on his farm he had some chicks, E-I-E-I-O, With a chick chick here, And a chick chick there, Here a chick, there a chick, Everywhere a chick chick, Old MacDonald had a farm, E-I-E-I-O, Old MACDONALD had a farm, E-I-E-I-O, And on his farm he had a duck, E-I-E-I-O, With a quack quack here, And a quack quack there, Here a quack, there a quack, Everywhere a quack quack, Old MacDonald had a farm, E-I-E-I-O, Old MACDONALD had a farm, E-I-E-I-O, And on his farm he had a pig, E-I-E-I-O, With a oink oink here, And a oink oink there, Here a oink, there a oink, Everywhere a oink oink, Old MacDonald had a farm, E-I-E-I-O, Old MacDonald had a farm, E-I-E-I-O, And on his farm he had a cow, E-I-E-I-O, With a moo moo here, And a moo moo there, Here a moo, there a moo, Everywhere a moo moo, Old MacDonald had a farm, E-I-E-I-O, Old MACDONALD had a farm, E-I-E-I-O, And on his farm he had some dogs, E-I-E-I-O, With a bow wow here, And a bow wow there, Here a bow wow, there a bow wow, Everywhere a bow wow, Old MacDonald had a farm, E-I-E-I-O, Old MACDONALD had a farm, E-I-E-I-O, And on his farm he had some donkeys, E-I-E-I-O, With a hee, haw here, And a hee, haw there, Here a hee, haw, there a hee, haw, Everywhere a hee, haw, Old MacDonald had a farm, E-I-E-I-O"
        dialog6.appendChild(oldmacLyric);
    };
    document.getElementById('hide6').onclick = function() {
        dialog6.close();
		dialog6.removeChild(oldmacLyric);
    };
}
showtextOldmac();

function showtextSpider() {
    var dialog7 = document.getElementById('dialog7');
    var spiderLyric = document.createElement("p");
	spiderLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show7').onclick = function() {
        dialog7.show();
        spiderLyric.innerText = "The itsy-bitsy spider, Climbed up the water spout, Down came the rain, And washed the spider out, Out came the sun-shine, And dried up all the rain, And itsy-bitsy spider, Climbed up the spout again"
        dialog7.appendChild(spiderLyric);
    };
    document.getElementById('hide7').onclick = function() {
        dialog7.close();
		dialog7.removeChild(spiderLyric);
    };
}
showtextSpider();

function showtextABC() {  
    var dialog3 = document.getElementById('dialog3');  
    var abclyric = document.createElement("p")
    abclyric.setAttribute("class", "lyricscroll")
    document.getElementById('show3').onclick = function() {  
        dialog3.show();  
        abclyric.innerText = "A - B - C - D - E - F - G - H - I - J - K - L - M - N - O - P - Q - R - S - T - U- V -W - X - Y and Z. Now I know my ABCs, Next time wont you sing with me.";
        dialog3.appendChild(abclyric);
    };  
    document.getElementById('hide3').onclick = function() {  
        dialog3.close();  
        dialog3.removeChild(abclyric);
    };  
}
showtextABC(); 

function showtextHappy() {
    var dialog8 = document.getElementById('dialog8');
    var happyLyric = document.createElement("p")
	happyLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show8').onclick = function() {
        dialog8.show();
        happyLyric.innerText = "If you're happy and you know it, clap your hands (clap clap), If you're happy and you know it, clap your hands (clap clap), If you're happy and you know it, and your really wanna show it,, If you're happy and you know it, clap your hands. (clap clap), If you're happy and you know it, stomp your feet (stomp stomp), If you're happy and you know it, stomp your feet (stomp stomp), If you're happy and you know it, and you really wanna show it,, If you're happy and you know it, stomp your feet. (stomp stomp), If you're happy and you know it, turn around (turn around), If you're happy and you know it, turn around (turn around), If you're happy and you know it, turn around (turn around), If you're happy and you know it, and you really wanna show it,, If you're happy and you know it, turn around (turn around), If you're happy and you know it, nod your head (nod your head), If you're happy and you know it, nod your head (nod your head), If you're happy and you know it, and you really wanna show it,, If you're happy and you know it, nod your head (nod your head), If you're happy and you know it, shake your legs (shake your legs), If you're happy and you know it, shake your legs (shake your legs), If you're happy and you know it, and you really wanna show it,, If you're happy and you know it, shake your legs (shake your legs), If you're happy and you know it, shake your legs (snap your fingers), If you're happy and you know it, shake your legs (snap your fingers), If you're happy and you know it, and you really wanna show it,, If you're happy and you know it, snap your fingers (snap your fingers), If you're happy and you know it, and you really wanna show it,, If you're happy and you know it, clap your hands! (clap clap)"
        dialog8.appendChild(happyLyric);
    };
    document.getElementById('hide8').onclick = function() {
        dialog8.close();
		dialog8.removeChild(happyLyric);
    };
}
showtextHappy();

function showtextWheels() {
    var dialog9 = document.getElementById('dialog9');
    var wheelsLyric = document.createElement("p")
	wheelsLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show9').onclick = function() {
        dialog9.show();
        wheelsLyric.innerText = "The wheels on the bus go round and round, Round and round, Round and round, The wheels on the bus go round and round, All through the town, The door on the bus go open and shut, Open and shut, Open and shut, The door on the bus go open and shut, All through the town, The wipers on the bus go Swish, swish, swish, Swish, swish, swish, Swish, swish, swish, The wipers on the bus go Swish, swish, swish, All through the town, The horn on the bus goes Beep, beep, beep, Beep, beep, beep, Beep, beep, beep, The horn on the bus goes Beep, beep, beep, All through the town, The people on the bus go up and down, Up and down, Up and down, The people on the bus go up and down, All through the town, The baby on the bus goes 'Wah, wah, wah,, Wah, wah, wah,, Wah, wah, wah', The baby on the bus goes 'Wah, wah, wah',, all through the town, The mommy on the bus says 'Shhh, Shhh, Shhh, Shhh, Shhh, Shhh,, Shhh, Shhh, Shhh, The daddy on the bus says 'Shhh, Shhh, Shhh', All through the town, The mommy on the bus says 'I love you', 'I love you', 'I love you', 'I love you', The daddy on the bus says 'I love you too', All through the town"
        dialog9.appendChild(wheelsLyric);
    };
    document.getElementById('hide9').onclick = function() {
        dialog9.close();
		dialog9.removeChild(wheelsLyric);
    };
}
showtextWheels();

function showtextDucks() {
    var dialog0 = document.getElementById('dialog0');
    var ducksLyric = document.createElement("p")
	ducksLyric.setAttribute("class", "lyricscroll")
    document.getElementById('show0').onclick = function() {
        dialog0.show();
        ducksLyric.innerText = "Five little ducks went swimming one day, Over the hills and far away, Mommy duck said, 'Quack quack quack quack', And only four little ducks came back! Four little ducks went swimming one day, Over the hills and far away, Mommy duck said, 'Quack quack quack quack', And only three little ducks came back! Three little ducks went swimming one day, Over the hills and far away, Mommy duck said, 'Quack quack quack quack', And only two little ducks came back! Two little ducks went swimming one day, Over the hills and far away., Mommy duck said, 'Quack quack quack quack', And only one little duck came back! One little duck went swimming one day, Over the hills and far away, Mommy duck said, 'Quack quack quack quack', but no little ducks came swimming back! No little ducks went swimming one day, Over the hills and far away, Daddy duck said, 'Quack quack quack quack', And all the five little ducks came back!"
        dialog0.appendChild(ducksLyric);
    };
    document.getElementById('hide0').onclick = function() {
        dialog0.close();
		dialog0.removeChild(ducksLyric);
    };
}
showtextDucks();


var showbutton2 = document.getElementById("show2")

showbutton2.addEventListener("mouseenter", function(e){
	showbutton2.style.color = "white";
})
showbutton2.addEventListener("mouseleave", function(e){
	showbutton2.style.color = "black";
})

var showbuttons = document.getElementsByClassName("showbutton")

for (i = 0; i < showbuttons.length; i++) {
	showbuttons[i].style.background = "orange"
}

document.getElementById("violin").addEventListener("click", function(){
    document.getElementById("audio1").play();
});
document.getElementById("piano").addEventListener("click", function(){
    document.getElementById("audio2").play();
});
document.getElementById("guitar").addEventListener("click", function(){
    document.getElementById("audio3").play();
});
document.getElementById("saxaphone").addEventListener("click", function(){
    document.getElementById("audio4").play();
});
document.getElementById("cello").addEventListener("click", function(){
    document.getElementById("audio5").play();
});
document.getElementById("trumpet").addEventListener("click", function(){
    document.getElementById("audio6").play();
});
document.getElementById("drums").addEventListener("click", function(){
    document.getElementById("audio7").play();
});
document.getElementById("clarinet").addEventListener("click", function(){
    document.getElementById("audio8").play();
});


var body = document.getElementsByTagName("body")[0]

var cardImage = document.getElementsByClassName("card-img-top")[0]
cardImage.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "blue"
})
cardImage.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage2 = document.getElementsByClassName("card-img-top")[1]
cardImage2.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "purple"
})
cardImage2.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage3 = document.getElementsByClassName("card-img-top")[2]
cardImage3.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "grey"
})
cardImage3.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage4 = document.getElementsByClassName("card-img-top")[3]
cardImage4.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "green"
})
cardImage4.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage4 = document.getElementsByClassName("card-img-top")[4]
cardImage4.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "orange"
})
cardImage4.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage4 = document.getElementsByClassName("card-img-top")[5]
cardImage4.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "black"
})
cardImage4.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage5 = document.getElementsByClassName("card-img-top")[6]
cardImage5.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "pink"
})
cardImage5.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage6 = document.getElementsByClassName("card-img-top")[7]
cardImage6.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "gold"
})
cardImage6.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})

var cardImage7 = document.getElementsByClassName("card-img-top")[8]
cardImage7.addEventListener("mouseenter", function(e){
	body.style.backgroundColor = "red"
})
cardImage7.addEventListener("mouseleave", function(e){
	body.style.backgroundColor = "lightblue"
})