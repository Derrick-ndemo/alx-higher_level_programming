$(document).ready(() => {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (data) =>  {
        $('DIV#hello').append(`${data["hello"]}`);
    });
});