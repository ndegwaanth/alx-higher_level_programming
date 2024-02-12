#!/usr/bin/node

const arg = process.argv[2];
const digit = parseInt(arg);

if (!isNaN(digit)) {
  console.log(`My number: ${digit}`);
} else {
  console.log('Not a number');
}
