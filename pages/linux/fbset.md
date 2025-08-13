# fbset

> Show and modify frame buffer device settings.
> More information: <https://manned.org/man/fbset.1>.

- Show current framebuffer settings:

`sudo fbset {{[-i|--info]}}`

- Set a framebuffer mode defined in `/etc/fb.modes`:

`sudo fbset "{{800}}x{{600}}-{{60}}"`
