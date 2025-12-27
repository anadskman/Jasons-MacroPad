// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬
     * │Ctrl│ 
     * ├───┼───┼───┼
     * │ X  │ C  │ V  │
     * ├───┼───┼───┼
     */
    [0] = LAYOUT(
        KC_LEFT_CTRL,
	KC_X, KC_C, KC_V
    )
};
