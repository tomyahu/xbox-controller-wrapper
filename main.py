from __future__ import print_function
from conf import buttons, absolute, refresh_time

import threading
import time

from inputs import get_gamepad
from aux_funs import PressButton, ReleaseButton, SetPressedKey, SetReleasedKey, moveMouseToRelative, pressed_keys, mouse_speed

released_keys = dict()

# The mutex for multithreaded structure handling (pressed keys)
lock = threading.Lock()

# Function that loops, taking the currently detected inputs of the
# controller and pressing the associated keys (or moving the mouse)
def inject_inputs():
	while 1:
		lock.acquire()
		
		# Presses the keys (or mouse button) mapped to the pressed buttons in the controller
		for key in pressed_keys.keys():
			if pressed_keys[key]:
				PressButton(key)
				released_keys[key] = False
			else:
				if not key in released_keys or not released_keys[key]:
					ReleaseButton(key)
					released_keys[key] = True
		
		# Moves the mouse
		moveMouseToRelative(int(mouse_speed[0]), int(mouse_speed[1]))
		
		lock.release()
		time.sleep(refresh_time)

def main():
	# Starts thread to press the associated mapped keys to the controller
	threading.Thread(target=inject_inputs).start()
	
	while 1:
		try:
			events = get_gamepad()
			
			# Checks the controller events
			for event in events:
				
				# A button in the contoller is pressed or released (not a trigger or analog)
				if event.ev_type == "Key":
					if event.code in buttons.keys():
						# The button is pressed
						if event.state == 1:
							lock.acquire()
							SetPressedKey(buttons[event.code])
							lock.release()
						# The button is released
						else:
							lock.acquire()
							SetReleasedKey(buttons[event.code])
							lock.release()
				# A trigger or analog in the controller is activated
				elif event.ev_type == "Absolute":
					if event.code in absolute.keys():
						lock.acquire()
						absolute[event.code](event.state)
						lock.release()
		except:
			pass


if __name__ == "__main__":
	main()