let statement = 'YeYe';
console.log(statement);

// Objects
let person = {
	name: 'Babe',
	age: 111,
	testFunc
};

person['name'] = 'dank';
console.log(person.name);

person.testFunc = function(num, num2) {console.log("test");};
// Better Syntax: let/const testFunc/person.testFunc = (num, num2) => {statement;}; 
person.testFunc;

// Arrays
let selectedColors = ['red','blue'];
console.log(selectedColors);

// Functions
function greet(name, funLevel = 'level1') {
	console.log('doggy, ' + name + funLevel);
}

function square(value) {
	return value * value;
}

let biggieChungas = prompt("Feed me");
// Without the breaks, the code just keeps executing
switch (biggieChungas.toLowerCase()) {	
	case "carrot":
		greet("Chunga", " Over 9000");
		break;
	case "steak":
		console.log("sies");
		break;
	default:
		console.log(biggieChungas + " is so good");
		break;
}

if (biggieChungas.toLowerCase == "secret") console.log("So big, Chunga Chunga"); 

let thisNum = Number(prompt("give me a number"));
if (21 > thisNum) {
	console.log(square(thisNum));
}
else if (21 === thisNum) {
	console.log(thisNum);
}
else {
	// While checks the condition first then executes
	while (thisNum > 0) {
		console.log(thisNum);
		thisNum -= 3;
	}
}

// Do while executes once first, then starts checking the condition
do {
	if (thisNum === 0) {
		console.log("Broken");
		break; // Ends execution
	}
	thisNum -= 0.5;
	if (thisNum === -2) {
		continue; // Jumps out of current loop iteration, and starts the next one
		console.log("This code will never be executed");
	}
	console.log(thisNum);
} while (thisNum > -3 && thisNum < 1);

/* 
 Words words words
*/

