var clickHandler = function (event) {
    console.log('You clicked on the ' + event.target.tagName);
};

var buttonHTML = '<button>Click me!</button>';
$('#foo').before(buttonHTML);
$('button').click(clickHandler);
