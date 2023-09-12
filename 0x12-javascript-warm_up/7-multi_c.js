#!/usr/bin/node
const repeatedString = 'C is fun';
const x = Number(process.argv[2]);

if (!isNaN(x) && Number.isInteger(x)) {
  for (let i = 0; i < x; i++) {
    console.log(repeatedString);
  }
} else {
  console.log('Missing number of occurrences');
}
