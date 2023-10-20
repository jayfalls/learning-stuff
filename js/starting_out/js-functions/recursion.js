function isEven(value = 0) {
	if (value === 0) return true;
	else if (value > -2 && value < 2) return false;
	
	let calc_num = 0;
	if (value > 0) calc_num += value - 2;
	else calc_num += value + 2;
	
	if (calc_num % 2 === 0) return true;
	else return false;
}

console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));
console.log(isEven(-20));
