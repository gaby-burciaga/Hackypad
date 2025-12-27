import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
]

keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

keyboard.keymap = [
    [
        KC.A,
        KC.S,
        KC.D,
        KC.W,
    ]
]

encoder = EncoderHandler()

encoder.pins = (
    (board.D7, board.D8)
)

encoder.map = [
    (KC.VOLU, KC.VOLD),
]

keyboard.modules.append(encoder)

i2c = busio.I2C(board.SCL, board.SDA)

display = Display(
    display=SSD1306(
        i2c=i2c,
        device_address=0x3C,
    )
    width=128,
    height=32,
    brightness=0.8
)

display.entries = [
    TextEntry(text="OMGGG", x=0, y=0),
]

keyboard.extensions.append(display)


if __name__ == "__main__":
    keyboard.go()
