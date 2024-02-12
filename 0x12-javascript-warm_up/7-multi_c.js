#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (!isNaN(number)) {
  for (let n = 0; n < number; n++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
