#!/usr/bin/node
const squareBuilder = 'X';
const squareSize = Number(process.argv[2]);

if (!isNaN(squareSize) && Number.isInteger(squareSize)) {
  for (let i = 0; i < squareSize; i++) {
    let row = '';

    for (let j = 0; j < squareSize; j++) {
      row += squareBuilder;
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
