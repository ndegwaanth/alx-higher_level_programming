#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (!isNaN(number)) {
  for (let m = 0; m < number; m++) {
    const row = 'X'.repeat(number);
    console.log(row);
  }
} else {
  console.log('Missing size');
}
