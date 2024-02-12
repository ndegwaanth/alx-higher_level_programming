#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Convert arguments to integers and sort them in descending order
const integers = args.map(Number).sort((a, b) => b - a);

// Check if there are no arguments or only one argument
if (integers.length === 0 || integers.length === 1) {
  console.log(0);
} else {
  // Find the second biggest integer
  const secondBiggest = integers[1];
  console.log(secondBiggest);
}
