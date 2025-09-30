# fbset

> Show and modify frame buffer device settings.
> More information: <https://manned.org/man/fbset.1>.

- Show current framebuffer settings:

`sudo fbset {{[-i|--info]}}`

- Set a framebuffer mode defined in `/etc/fb.modes`:

`sudo fbset "{{800}}x{{600}}-{{60}}"`

- Set an arbitrary framebuffer mode:

`sudo fbset {{[-g|--geometry]}} {{TTY_horizontal}} {{TTY_vertical}} {{monitor_horizontal}} {{monitor_vertical}} {{color_depth}}`
