from keys import *
from gamepad_events import *
from aux_funs import SimulateButton, SimulateButton2, SimulateMouseMoveX, SimulateMouseMoveY


# =======================================================================================================
buttons = dict()

# Here you can configure the buttons in the controller
# Example:
#		To map a button to the letter U in your keyboard for example replace
#		the value of the button to DIK_U
#
# DIK_<keyboard letter> are the keyboard keys
# MOUSE_LEFT_BUTTON and MOUSE_RIGHT_BUTTON also exist and are kind of self explanatory
# More keys are in the keys.py file, there are no more mouse buttons however
buttons[GAMEPAD_A] = MOUSE_LEFT_BUTTON
buttons[GAMEPAD_B] = MOUSE_RIGHT_BUTTON
buttons[GAMEPAD_X] = DIK_E
buttons[GAMEPAD_Y] = DIK_R
buttons[GAMEPAD_START] = DIK_T
buttons[GAMEPAD_SELECT] = DIK_Y
buttons[GAMEPAD_R1] = DIK_U
buttons[GAMEPAD_L1] = DIK_I

# =======================================================================================================
absolute = dict()

# Here you can configure the triggers, analogs and the plus pad in the controller
# As this are not just buttons some functions were made for them to behave as buttons
#
# Functions:
#		SimulateButton(keyboard_key_constant, threshold)
#			Created for triggers specifically
#			keyboard_key_constant: is a constant from keys.py
#			threshold: is a number that represents how pressed a trigger is,
#						when the trigger passes this value, the key given by
#						keyboard_key_constant is pressed, otherwise it is released
#
#		SimulateButton2(keyboard_key_constant1, keyboard_key_constant2, threshold)
#			Created for analogs and the plus pad specifically
#			keyboard_key_constant1: is a constant from keys.py
#			keyboard_key_constant2: is a constant from keys.py
#			threshold: is a number that represents how activated a trigger is,
#						when the trigger passes this value the key given by
#						keyboard_key_constant1 is pressed; when the trigger's
#						value is lower than threshold*(-1) the key given by
#						keyboard_key_constant2 is pressed; otherwise both keys
#						are released.
#
#		SimulateMouseMoveX(mouse_speed, threshold)
#			Created for analogs and the plus pad specifically
#			mouse_speed: is a number that represents the speed of the mouse,
#						this value is ponderated with how activated the
#						trigger is to get the real speed.
#			threshold: is a number that represents how activated a trigger is,
#						when the trigger passes this value, the mouse moves
#						in x to the right; when the trigger's value is lower
#						than threshold*(-1) the mouse moves in x to the right.
#
#		SimulateMouseMoveY is the same as SimulateMouseMoveY but made for the y axis of analogs and the plus pad
#
absolute[GAMEPAD_R2] = SimulateButton(DIK_A, 255) # value of GAMEPAD_R2 can be between 0 and 255
absolute[GAMEPAD_L2] = SimulateButton(DIK_S, 255) # value of GAMEPAD_L2 can be between 0 and 255
absolute[GAMEPAD_PLUS_PAD_X] = SimulateButton2(DIK_A, DIK_D, 1) # value of GAMEPAD_PLUS_PAD_X can be -1, 0 or 1 (left is -1, right is 1)
absolute[GAMEPAD_PLUS_PAD_Y] = SimulateButton2(DIK_W, DIK_S, 1) # value of GAMEPAD_PLUS_PAD_X can be -1, 0 or 1 (up is -1, down is 1)
absolute[GAMEPAD_LEFT_ANALOG_X] = SimulateButton2(DIK_A, DIK_D, 10000) # value of GAMEPAD_LEFT_ANALOG_X can be between -32767 and 32767
absolute[GAMEPAD_LEFT_ANALOG_Y] = SimulateButton2(DIK_S, DIK_W, 10000) # value of GAMEPAD_LEFT_ANALOG_Y can be between -32767 and 32767
absolute[GAMEPAD_RIGHT_ANALOG_X] = SimulateMouseMoveX(25, 10000) # value of GAMEPAD_RIGHT_ANALOG_X can be between -32767 and 32767
absolute[GAMEPAD_RIGHT_ANALOG_Y] = SimulateMouseMoveY(-25, 10000) # value of GAMEPAD_RIGHT_ANALOG_Y can be between -32767 and 32767

# =======================================================================================================
# The interval of time the buttons are checked to press the mapped keys
refresh_time = 1/60