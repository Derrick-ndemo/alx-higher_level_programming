$(document).ready(function() {
    $('#btn_translate').click(function() {
        let language = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + language, function(data) {
            $('#hello').text(data.hello);
        });
    });
});