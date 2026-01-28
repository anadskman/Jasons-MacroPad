import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

# Use D1–D4 for your buttons
PINS = [board.RX, board.SCK, board.MOSI, board.MISO]

# Single-row scanner for 4 keys
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=True,  # True if button connects to GND
)

# Keymap: each button types a letter
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == "__main__":
    keyboard.go()
