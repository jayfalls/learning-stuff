function min(value1 = 0, value2 = 0) {
	if (value1 === value2 || value1 < value2) return value1;
	else return value2;
}

console.log(min(-1,20));
console.log(min(50,50));
console.log(min(765,764));
