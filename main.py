import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.matrix import MatrixScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

#MATRIX PINS
# Columns go to XIAO A0, A1, A2, A3
COL_PINS = [board.A0, board.A1, board.A2, board.A3]

# Rows go to XIAO GP6, GP7, GP0, GP1
ROW_PINS = [board.GP6, board.GP7, board.GP0, board.GP1]

#MATRIX SETUP
#diodes point from column → row (COL2ROW)
keyboard.matrix = MatrixScanner(
    columns=COL_PINS,
    rows=ROW_PINS,
    diode_orientation=DiodeOrientation.COLUMNS,
)

#KEYMAP
# 16 Keys arranged row by row
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,        # Row 0: SW1–SW4
        KC.E, KC.F, KC.G, KC.H,        # Row 1: SW5–SW8
        KC.I, KC.J, KC.K, KC.L,        # Row 2: SW9–SW12
        KC.M, KC.N, KC.O, KC.P,        # Row 3: SW13–SW16
    ]
]

if __name__ == '__main__':
    keyboard.go()