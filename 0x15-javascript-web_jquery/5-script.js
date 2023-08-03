$(document).ready(() => {
    $('DIV#add_item').on('click', () => {
        $('UL.my_list').append(`<li>Item</li>`);
    });
});