# fbset

> Show and modify frame buffer device settings.
> More information: <https://manned.org/fbset.1>.

- Show current framebuffer settings:

`sudo fbset {{[-i|--info]}}`

- Set a framebuffer mode defined in `/etc/fb.modes`:

`sudo fbset "{{800}}x{{600}}-{{60}}"`

- Set the dimensions of the framebuffer:

`sudo fbset -xset {{horizontal_pixels}} -yset {{vertical_pixels}}`

- Set an arbitrary framebuffer mode:

`sudo fbset {{[-g|--geometry]}} {{TTY_horizontal}} {{TTY_vertical}} {{monitor_horizontal}} {{monitor_vertical}} {{color_depth}}`
