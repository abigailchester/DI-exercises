console.log(1 + 1);

console.log('hello' + ' ' + ' concat' + ' ' + 'hello')

var x = 1;
var y = 2;
console.log(x+y);

x = "is a string"

console.log(x)
console.log(x + y)

let a = 5;
console.log(a);

const b = 9;
console.log('b',b);
// b = 10

let t = 1;
let r = 2;

if (true) {
	console.log('true');
}

if (t==r) {
	console.log('true');
}
else {
	console.log('false');
}

if (t===r) {
	let c = 9;
	let d = t + c;
	console.log(d);
}
else if (t==2) {
	console.log(hi);
}

else {
	let z= 10;
	let v = z + t;
	console.log(v);
}

// let u = 'main';

// switch ('main')

let g = 4.98364856;

console.log(g.toFixed(0));
console.log(g.toFixed(3));
g.toFixed(1);


var txt = "wfgjwhregfkqurkgfurhfbfr";

var j = txt.length;

console.log(j);

//prints 24

let param1 = prompt('This is the prompt message')
console.log(param1);

//get 3 inputs --> number, then + or -, then another number

let num1 = prompt('enter number here');
console.log(num1);

let sign = prompt('enter + or -');
console.log(sign);

let num2 = prompt('enter another number here');
console.log(num2);

if (sign === '-') {
	alert(num1-num2);
}

else if(sign === '+'){
	alert(num1+num2);
}

else{
	alert('You did not enter correctly')
}


switch(sign) {
	case '+':
		alert(num1+num2)
		break;
	case '-':
		alert(num1-num2)
		break;
	default:
		alert('you did not enter correct')

}

// let x = (sign==='+') ? (num1+num2) : (num1-num2);
// alert(x);


// if(sign==='+' && sign !=''){

// }









