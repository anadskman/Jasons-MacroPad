import board, busio
import adafruit_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

PINS = [board.RX, board.SCK, board.MOSI, board.MISO]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  
)

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

Select = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.A),
    Release(KC.LCTL)
)

Cut = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.X),
    Release(KC.LCTL)
)

Copy = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

Paste = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
    )

# Keymap: each button types a letter
keyboard.keymap = [
    [Select, Cut, Copy, Paste]
]


 #---- Rotary Encoder ----
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.SDA, board.SCL),  # Encoder A, B
)

encoder.map = [
    (KC.VOLD, KC.VOLU),
]

if __name__ == "__main__":

    keyboard.go()