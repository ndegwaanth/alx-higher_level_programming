import $ from 'jquery';

$('document').ready(function () {
  $('DIV#red_heade').click(function () {
    document.getElementsByTagName('header')[0].classList.add('red');
  });
});
