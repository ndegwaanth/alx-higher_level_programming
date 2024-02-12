#!/usr/bin/node

const argcount = process.argv.length - 2;

if (argcount === 0) {
  console.log('No argument');
} else if (argcount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
