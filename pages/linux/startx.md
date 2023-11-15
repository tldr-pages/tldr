# startx

> A front-end to `xinit` that provides a nice user interface for running a single session of the X Window System.
> More information: <https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>.

- Start an X session:

`startx`

- Start an X session with a predefined depth value:

`startx -- -depth {{value}}`

- Start an X session with a predefined dpi value:

`startx -- -dpi {{value}}`

- Override the settings in the `.xinitrc` file and start a new X session:

`startx /{{path/to/window_manager_or_desktop_environment}}`
