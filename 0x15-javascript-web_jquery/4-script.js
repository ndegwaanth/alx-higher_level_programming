import $ from 'jquery';

// Execute when the document is fully loaded
$(document).ready(function () {
  // Bind click event to the element with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Toggle the class 'red' and 'green' on the <header> element
    $('header').toggleClass('red green');
  });
});
