#!/usr/bin/node

function factorial (n) {
  if (n <= 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = parseInt(process.argv[2]);

console.log(factorial(number));
