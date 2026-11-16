# Using ST7789 display with MicroPython

ddd

## Ressources and references

* [Pure FrameBuffer ST7789 implementation for MicroPython](https://github.com/easytarget/st7789-framebuffer)
* [NO FramBuffer ST7789 implementation for MicroPython](https://github.com/halherta/st7789_lcd_driver_micropython/blob/main/README.md) write directly into display memory. Advanced driver version.
* [NO FrameBuffer ST7789 rudimentary implementation](https://github.com/devbis/st7789py_mpy/tree/master)

# Color Palette

Display uses RGB565 color. Here is a snip of code to define the color palette.

``` python
# An example 'palette' class with 20 colors and helper
class palette():
    # color definitions
    BLACK    = 0x0000
    DARKGREY = 0x4208
    NAVY     = 0x0010
    BLUE     = 0x001f
    GREEN    = 0x0400
    TEAL     = 0x0410
    AZURE    = 0x041f
    LIME     = 0x07e0
    CYAN     = 0x07ff
    MAROON   = 0x8000
    PURPLE   = 0x8010
    OLIVE    = 0x8400
    GREY     = 0x8410
    SILVER   = 0xc618
    RED      = 0xf800
    ROSE     = 0xf810
    MAGENTA  = 0xf81f
    ORANGE   = 0xfc00
    YELLOW   = 0xffe0
    WHITE    = 0xffff
    # color helper
    color565 = st7789.color565
    swap_bytes = st7789.swap_bytes
```