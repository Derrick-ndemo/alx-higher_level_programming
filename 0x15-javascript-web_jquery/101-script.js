$(document).ready(() => {
    $('DIV#add_item').click(() => {
        $('.my_list').append(`<li>Item</li>`);
    });
    $('DIV#remove_item').click(() => {
        $('.my_list li:last').remove();
    });
    $('DIV#clear_list').click(() => {
        $('.my_list').hide();
    });
});