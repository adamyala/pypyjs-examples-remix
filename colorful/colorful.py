import js
import math

document = js.globals['document']
window = js.globals['window']
ratio_closest = 0


@js.Function
def on_mouse_move(event):
    color_map = mouse_position(event)
    change_background_color(color_map)


document.onmousemove = on_mouse_move


@js.Function
def mouse_position(event):
    body = document['body']
    mouse_x = float(event['clientX'] + body['scrollLeft'])
    mouse_y = float(event['clientY'] + body['scrollTop'])
    window_width = float(window['innerWidth'])
    window_height = float(window['innerHeight'])

    show = document['show']
    show['mouseXField']['value'] = mouse_x
    show['mouseYField']['value'] = mouse_y
    show['windowWidth']['value'] = window_width
    show['windowHeight']['value'] = window_height

    x_center = window_width / 2
    y_center = window_height / 2

    relative_cursor_x = x_center - mouse_x
    relative_cursor_y = y_center - mouse_y

    theta_point = math.atan2(relative_cursor_y, relative_cursor_x)
    absolute_theta_point = abs(theta_point)

    minus_60_x = (relative_cursor_x * math.cos(-60) - relative_cursor_y * math.sin(-60))
    minus_60_y = (relative_cursor_x * math.sin(-60) + relative_cursor_y * math.cos(-60))
    minus_theta_point = math.atan2(minus_60_y, minus_60_x)
    absolute_minus_theta_point = abs(minus_theta_point)

    plus_60_x = (relative_cursor_x * math.cos(60) - relative_cursor_y * math.sin(60))
    plus_60_y = (relative_cursor_x * math.sin(60) + relative_cursor_y * math.cos(60))
    plus_theta_point = math.atan2(plus_60_y, plus_60_x)
    absolute_plus_theta_point = abs(plus_theta_point)

    x_squared = math.pow(relative_cursor_x, 2)
    y_squared = math.pow(relative_cursor_y, 2)
    point_squared = x_squared + y_squared
    distance_to_origin = math.sqrt(point_squared)

    # global color_r_preround
    color_r_preround = (absolute_theta_point / math.pi) * 255
    # global color_b_preround
    color_b_preround = (absolute_minus_theta_point / math.pi) * 255
    # global color_y_preround
    color_y_preround = (absolute_plus_theta_point / math.pi) * 255

    global ratio_closest
    if window_height >= window_width:
        distance = window_width
    else:
        distance = window_height
    ratio_closest = 2.0 * distance_to_origin / distance

    return {
        'r': color_r_preround,
        'b': color_b_preround,
        'y': color_y_preround,
    }


@js.Function
def change_background_color(color_map):
    intensity = 0.5 - ratio_closest

    @js.Function
    def color_intensify(color_value):
        intensified_color = color_value + (intensity * 255)
        if intensified_color >= 255:
            return 255
        elif intensified_color <= 0:
            return 0
        else:
            return int(intensified_color)

    color_r = color_intensify(color_map['r'])
    color_b = color_intensify(color_map['b'])
    color_y = color_intensify(color_map['y'])

    # base 16 encode the color as hex
    color_r_hex = format(int(color_r), 'x')
    color_b_hex = format(int(color_b), 'x')
    color_y_hex = format(int(color_y), 'x')

    color_combined = '#{}{}{}'.format(color_r_hex, color_b_hex, color_y_hex)

    background_element = document.getElementById('body')
    background_element['style']['background'] = color_combined

    show = document['show']
    show['colorg']['value'] = color_combined
    show['distToOrigin']['value'] = intensity
