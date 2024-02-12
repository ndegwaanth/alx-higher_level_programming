#!/usr/bin/node

// Define the callMeMoby function
function callMeMoby (x, theFunction) {
  // Loop x times and call the given function each time
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the callMeMoby function so that it's visible from outside
module.exports.callMeMoby = callMeMoby;
