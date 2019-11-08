import ctypes
import time
from keys import *

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
	_fields_ = [("wVk", ctypes.c_ushort),
				("wScan", ctypes.c_ushort),
				("dwFlags", ctypes.c_ulong),
				("time", ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
	_fields_ = [("uMsg", ctypes.c_ulong),
				("wParamL", ctypes.c_short),
				("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
	_fields_ = [("dx", ctypes.c_long),
				("dy", ctypes.c_long),
				("mouseData", ctypes.c_ulong),
				("dwFlags", ctypes.c_ulong),
				("time",ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
	_fields_ = [("ki", KeyBdInput),
				 ("mi", MouseInput),
				 ("hi", HardwareInput)]

class Input(ctypes.Structure):
	_fields_ = [("type", ctypes.c_ulong),
				("ii", Input_I)]

# Actuals Functions
def PressKey(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



from ctypes import windll, Structure, c_long, byref

class POINT(Structure):
	_fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
	pt = POINT()
	windll.user32.GetCursorPos(byref(pt))
	return pt

def moveMouseTo(x, y):
	ctypes.windll.user32.SetCursorPos(x, y)

def moveMouseToRelative(vx, vy):
	mouse_pos = queryMousePosition()
	ctypes.windll.user32.SetCursorPos(mouse_pos.x + vx, mouse_pos.y + vy)



pressed_keys = dict()
def SetPressedKey(hexKeyCode):
	pressed_keys[hexKeyCode] = True

def SetReleasedKey(hexKeyCode):
	pressed_keys[hexKeyCode] = False

def SimulateButton(button, activationDelta):
	def aux_fun(val):
		if val >= activationDelta:
			SetPressedKey(button)
		else:
			SetReleasedKey(button)
	
	return aux_fun

def SimulateButton2(negativeButton, positiveButton, activationDelta):
	def aux_fun(val):
		if val >= activationDelta:
			SetPressedKey(positiveButton)
		elif val <= -activationDelta:
			SetPressedKey(negativeButton)
		else:
			SetReleasedKey(positiveButton)
			SetReleasedKey(negativeButton)
	
	return aux_fun

mouse_speed = [0,0]
def SimulateMouseMoveX(speed, activationDelta):
	def aux_fun(val):
		total_move = speed * (abs(val) - activationDelta) / (32768.0-activationDelta)
		if val >= activationDelta:
			mouse_speed[0] = total_move
		elif val <= -activationDelta:
			mouse_speed[0] = -total_move
		else:
			mouse_speed[0] = 0
	
	return aux_fun

def SimulateMouseMoveY(speed, activationDelta):
	def aux_fun(val):
		total_move = speed * (abs(val) - activationDelta) / (32768.0-activationDelta)
		if val >= activationDelta:
			mouse_speed[1] = total_move
		elif val <= -activationDelta:
			mouse_speed[1] = -total_move
		else:
			mouse_speed[1] = 0
	
	return aux_fun

pressed_clicks = dict()
pressed_clicks["left"] = False
pressed_clicks["right"] = False

def PressLeftMouseButton():
	if not pressed_clicks["left"]:
		ctypes.windll.user32.mouse_event(0x02, 0, 0, 0, 0)
		pressed_clicks["left"] = True

def ReleaseLeftMouseButton():
	if pressed_clicks["left"]:
		ctypes.windll.user32.mouse_event(0x04, 0, 0, 0, 0)
		pressed_clicks["left"] = False

def PressRightMouseButton():
	if not pressed_clicks["right"]:
		ctypes.windll.user32.mouse_event(0x08, 0, 0, 0, 0)
		pressed_clicks["right"] = True

def ReleaseRightMouseButton():
	if pressed_clicks["right"]:
		ctypes.windll.user32.mouse_event(0x10, 0, 0, 0, 0)
		pressed_clicks["right"] = False

def PressButton(button):
	if button == MOUSE_LEFT_BUTTON:
		PressLeftMouseButton()
	elif button == MOUSE_RIGHT_BUTTON:
		PressRightMouseButton()
	else:
		PressKey(button)

def ReleaseButton(button):
	if button == MOUSE_LEFT_BUTTON:
		ReleaseLeftMouseButton()
	elif button == MOUSE_RIGHT_BUTTON:
		ReleaseRightMouseButton()
	else:
		ReleaseKey(button)

