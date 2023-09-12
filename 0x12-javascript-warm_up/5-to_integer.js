#!/usr/bin/node
const convertedArg = Number(process.argv[2]);
if (!isNaN(convertedArg) && Number.isInteger(convertedArg)) {
  console.log('My number: ' + convertedArg);
} else {
  console.log('Not a number');
}
