import evdev
from evdev import *

class Keyboard():
	def __init__(self):

		print ("waiting for keyboard")

		#keep trying to key a keyboard
		have_dev=False
		while have_dev==False:
			try:
				#try and get a keyboard - should always be event0 as
				#we're only plugging one thing in
				self.dev = evdev.InputDevice("/dev/input/event1")
				have_dev=True
			except OSError:
				print ("Keyboard not found, waiting 3 seconds and retrying")
				time.sleep(3)
			print ("found a keyboard")

		
	def event_loop(self):
		for event in self.dev.read_loop():
			print(event)


if __name__ == "__main__":
	print ("Setting up keyboard")

	kb = Keyboard()

	print ("starting event loop")
	kb.event_loop()


