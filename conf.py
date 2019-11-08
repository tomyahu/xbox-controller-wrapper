from keys import *
from gamepad_events import *
from aux_funs import SimulateButton, SimulateButton2, SimulateMouseMoveX, SimulateMouseMoveY

buttons = dict()

buttons[GAMEPAD_A] = MOUSE_LEFT_BUTTON
buttons[GAMEPAD_B] = MOUSE_RIGHT_BUTTON
buttons[GAMEPAD_X] = DIK_E
buttons[GAMEPAD_Y] = DIK_R
buttons[GAMEPAD_START] = DIK_T
buttons[GAMEPAD_SELECT] = DIK_Y
buttons[GAMEPAD_R1] = DIK_U
buttons[GAMEPAD_L1] = DIK_I

absolute = dict()

absolute[GAMEPAD_R2] = SimulateButton(DIK_A, 255) # Segundo numero puede ser entre 0 y 255
absolute[GAMEPAD_L2] = SimulateButton(DIK_S, 255) # Segundo numero puede ser entre 0 y 255

absolute[GAMEPAD_DIRX] = SimulateButton2(DIK_A, DIK_D, 1) # Tercer numero puede ser entre 0 y 1
absolute[GAMEPAD_DIRY] = SimulateButton2(DIK_W, DIK_S, 1) # Tercer numero puede ser entre 0 y 1

absolute[GAMEPAD_LEFT_ANALOG_X] = SimulateButton2(DIK_A, DIK_D, 10000) # Tercer numero puede ser entre -65255 y 65255
absolute[GAMEPAD_LEFT_ANALOG_Y] = SimulateButton2(DIK_W, DIK_S, 10000) # Tercer numero puede ser entre -65255 y 65255

absolute[GAMEPAD_RIGHT_ANALOG_X] = SimulateMouseMoveX(100, 10000) # Primer numero es la velocidad, Segundo numero puede ser entre -65255 y 65255
absolute[GAMEPAD_RIGHT_ANALOG_Y] = SimulateMouseMoveY(-100, 10000) # Primer numero es la velocidad, Segundo numero puede ser entre -65255 y 65255

refresh_time = 1/60