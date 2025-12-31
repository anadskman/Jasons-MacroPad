import time
import pyperclip
from pywinusb import hid

VID = 0xFEED
PID = 0x0000

# Find the keyboard device
all_devices = hid.HidDeviceFilter(vendor_id=VID, product_id=PID).get_devices()
if not all_devices:
    raise Exception("Macro pad not found!")

keyboard = all_devices[0]
keyboard.open()

last_text = ""

def send_clipboard(text):
    # Send up to 63 chars
    data = [0] + list(text.encode("utf-8")[:63])
    data += [0] * (64 - len(data))  # pad to 64 bytes
    keyboard.send_output_report(data)

try:
    while True:
        current = pyperclip.paste()
        if current != last_text:
            last_text = current
            print("Sending:", current)
            send_clipboard(current)
        time.sleep(0.2)
except KeyboardInterrupt:
    keyboard.close()
    print("Stopped")
