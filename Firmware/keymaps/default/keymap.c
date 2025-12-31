#include QMK_KEYBOARD_H
#include <string.h>


#define CLIP_MAX_LEN 64
char clipboard_text[CLIP_MAX_LEN] = "Nothing yet";
uint8_t scroll_offset = 0;


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_LEFT_CTRL,
        KC_X, KC_C, KC_V
    )
};


bool encoder_update_user(uint8_t index, bool clockwise) {
    if (clockwise) {
        if (scroll_offset < CLIP_MAX_LEN - 1) scroll_offset++;
    } else {
        if (scroll_offset > 0) scroll_offset--;
    }
    return true;
}


#ifdef OLED_ENABLE
bool oled_task_user(void) {
    oled_clear();
    oled_write_ln(PSTR("CLIPBOARD"), false);
    oled_write_ln(PSTR("--------"), false);
    oled_write(clipboard_text + scroll_offset, false);
    return false;
}
#endif


#ifdef RAW_ENABLE
void raw_hid_receive(uint8_t *data, uint8_t length) {
    memset(clipboard_text, 0, CLIP_MAX_LEN);
    memcpy(clipboard_text, data, length > CLIP_MAX_LEN ? CLIP_MAX_LEN : length);
    scroll_offset = 0;
}
#endif
