import $ from 'jquery';

$('document').ready(function () {
  $('DIV#red_heade').click(function () {
    $('header').css({
      color: '#FF0000'
    });
  });
});
