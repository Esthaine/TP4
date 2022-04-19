var2 = 0

def on_button_pressed_b():
    basic.show_string("" + str((input.temperature())))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global var2
    var2 = input.light_level()
basic.forever(on_forever)

#exo2
is_logo_pressed = False
def on_forever():
    global is_logo_pressed
    is_logo_pressed = True
    if input.logo_is_pressed():
        is_logo_pressed = False
    if is_logo_pressed == True:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

#exo3
def on_sound_loud():
    basic.show_icon(IconNames.SMALL_HEART)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

