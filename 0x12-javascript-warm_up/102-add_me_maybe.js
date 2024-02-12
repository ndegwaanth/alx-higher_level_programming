#!/usr/bin/node

// Define the addMeMaybe function
function addMeMaybe(number, theFunction) {
  // Increment the number
  number++;

  // Call the given function with the incremented number as an argument
  theFunction(number);
}

// Export the addMeMaybe function so that it's visible from outside
module.exports.addMeMaybe = addMeMaybe;
