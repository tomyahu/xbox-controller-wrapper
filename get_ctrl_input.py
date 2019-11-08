from __future__ import print_function
from conf import buttons, absolute

import threading
import time

from inputs import get_gamepad
from aux_funs import PressButton, ReleaseButton, SetPressedKey, SetReleasedKey, moveMouseToRelative, pressed_keys, mouse_speed

released_keys = dict()

lock = threading.Lock()

def inject_inputs():
	while 1:
		lock.acquire()
		for key in pressed_keys.keys():
			if pressed_keys[key]:
				PressButton(key)
				released_keys[key] = False
			else:
				if not key in released_keys or not released_keys[key]:
					ReleaseButton(key)
					released_keys[key] = True
		moveMouseToRelative(int(mouse_speed[0]), int(mouse_speed[1]))
		lock.release()
		time.sleep(1/60)

def main():
	threading.Thread(target=inject_inputs).start()
	
	while 1:
		try:
			events = get_gamepad()
			for event in events:
				if event.ev_type == "Key":
					if event.code in buttons.keys():
						if event.state == 1:
							lock.acquire()
							SetPressedKey(buttons[event.code])
							lock.release()
						else:
							lock.acquire()
							SetReleasedKey(buttons[event.code])
							lock.release()
				elif event.ev_type == "Absolute":
					if event.code in absolute.keys():
						lock.acquire()
						absolute[event.code](event.state)
						lock.release()
		except:
			pass


if __name__ == "__main__":
	main()