import board, busio
import adafruit_ssd1306
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from oled_encoder_module import OLEDEncoderModule


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


# OLED setup
i2c = busio.I2C(board.A1, board.A0)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)
oled.fill(0)
oled.show()

# Clipboard buffer
keyboard.clip_buffer = [
    "Line 1 hello",
    "Line 2 test",
    "Line 3 test",
    "Line 4 test",
    "Line 5 test",
    "Line 6 test",
]

# Add encoder module
encoder_module = OLEDEncoderModule(oled, board.SDA, board.SCL)
keyboard.modules.append(encoder_module)
encoder_module.update_oled(keyboard.clip_buffer)




if __name__ == "__main__":
    keyboard.go()