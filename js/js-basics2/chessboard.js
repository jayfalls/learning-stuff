function genChessGrid(gridSize = 8) {
	for (let y = 0; y < gridSize; y++) {
		let gridLine = "";
		let modulo;
		if (y % 2 === 0) modulo = 0;
		else modulo = 1;
		for (let x = 0; x < gridSize; x++) {	
			if (x % 2 === modulo) gridLine += " ";
			else gridLine += "#";
		}
		console.log(gridLine);
	}
}

// Initialisation
let gridSize = Number(prompt("Input a grid size, leave blank for default"));
if (typeof(gridSize) != Number) genChessGrid();
else genChessGrid(gridSize);
