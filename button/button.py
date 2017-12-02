# import our pypyjs dependency
import js


# decorating our python function makes it accessible as a click handler
@js.Function
def click_handler(event):
    print('You clicked on the ' + str(event.target.tagName))


# store the jquery object in python so we can interact with it
jquery = js.globals['$']

# typical javascript like interaction but in python!!!
button_html = '<button>Click me!</button>'
jquery('#foo').before(button_html)
jquery('button').click(click_handler)
