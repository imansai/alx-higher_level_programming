#!/usr/bin/node
const num = Number(process.argv[2]);

function factorial(num) {
  let result = 1;
  for (let i = 0; i < num ; i++) {
	result *= num-i;
  }
  console.log(result);
}

factorial(num);
