# Test ST7789 on 320x200 display - Basic demonstration using
#
# See Project: https://github.com/mchobby/st7789
#
#
from machine import SPI, Pin
from st7789 import ST7789_SPI

spi = SPI(1, miso=Pin(8), mosi=Pin(11), sck=Pin(10), baudrate=50_000_000 )
cs = Pin(9,Pin.OUT,True)
dc = Pin(12,Pin.OUT) # Data/Command
rst = Pin(13,Pin.OUT,True)
backlight = None # Can be Pin or PWN
bright = True # 0..1 for PWM
rot = 1 # 0-Portrait, 1-Landscape, 2-Inverted Portrait, 3-Inverted Landscape

lcd = ST7789_SPI( spi, 240, 320, rst, cs, dc, backlight, bright, rot, "RGB"  )

CYAN = 0x07ff
BLACK= 0x0000

lcd.fill( CYAN )
lcd.text( 'top-left', 0, 0, BLACK )
lcd.text( 'rotate=1', 0, 10, BLACK )

lcd.show()