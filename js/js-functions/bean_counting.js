function countBs(text) {
	let count = 0;
	for (let i = 0; i < text.length; i++) {
		if (text[i] === "B") count++;
	}
	return count;
}

function countChars(text,character) {	
	if (character.length > 1) return -1;
	let count = 0;
	for (let i = 0; i < text.length; i++) {
		if (text[i] === character) count++;
	}
	return count;
}

console.log(countBs("Blubberinng BluBB blub"));
console.log(countChars("Concatenate CaCkeys cliCk", "C"));
console.log(countChars("wwww","false"));
