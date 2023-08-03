$(document).ready(function() {
    function translate() {
        let language = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/?lang=' + language, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translate);

    $('#language_code').keypress(function(event) {
        let keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){ // 13 is the keycode for the Enter key
            translate();
        }
    });
});