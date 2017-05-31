
// Copying a short link to the clipboard.
var button_copy = document.querySelector('.to_clipboard');
if (button_copy) {
    button_copy.addEventListener('click', function (event) {
        var short_link = document.querySelector('#short_link');
        var range = document.createRange();
        range.selectNode(short_link);
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
        short_link.style.color = '#368bb9';
    });
}
