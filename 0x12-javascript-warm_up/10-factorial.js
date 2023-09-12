#!/usr/bin/node
const num = Number(process.argv[2]);

function factorial (num) {
  let result = 1;
  if (!isNaN(num)) {
    for (let i = 0; i < num; i++) {
      result *= num - i;
    }
    console.log(result);
  } else {
    console.log(result);
  }
}

factorial(num);
