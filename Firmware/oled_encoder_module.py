from kmk.modules import Module
import digitalio
import time

class OLEDEncoderModule(Module):
    def __init__(self, oled, pin_a, pin_b):
        self.oled = oled

        self.encoder_a = digitalio.DigitalInOut(pin_a)
        self.encoder_a.direction = digitalio.Direction.INPUT
        self.encoder_a.pull = digitalio.Pull.UP

        self.encoder_b = digitalio.DigitalInOut(pin_b)
        self.encoder_b.direction = digitalio.Direction.INPUT
        self.encoder_b.pull = digitalio.Pull.UP

        self.last_a = self.encoder_a.value
        self.scroll_index = 0
        self.last_time = time.monotonic()

    def before_matrix_scan(self, keyboard):
        now = time.monotonic()
        if now - self.last_time < 0.002:  # fast debounce
            return

        a = self.encoder_a.value
        b = self.encoder_b.value

        if a != self.last_a:
            # correct quadrature direction
            if b != a:
                self.scroll_index += 1
            else:
                self.scroll_index -= 1

            if hasattr(keyboard, "clip_buffer"):
                max_index = max(len(keyboard.clip_buffer) - 4, 0)
                self.scroll_index = max(0, min(self.scroll_index, max_index))
                self.update_oled(keyboard.clip_buffer)

            self.last_time = now

        self.last_a = a

    def update_oled(self, clip_buffer):
        self.oled.fill(0)
        for i in range(4):
            idx = self.scroll_index + i
            if idx < len(clip_buffer):
                self.oled.text(clip_buffer[idx][:21], 0, i * 8, 1)
        self.oled.show()
