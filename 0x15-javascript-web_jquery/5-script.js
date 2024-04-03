import $ from 'jquery';

$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    /* Append the new <li> element to the list with class 'my_list' */
    $('ul.my_list').append(newItem);
  });
});
