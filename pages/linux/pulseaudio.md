# pulseaudio

> The pulseaudio sound system daemon and manager.

- Check if pulseaudio is running (a non-zero exit code means it is not running):

`pulseaudio --check`

- Start the pulseaudio daemon in the background:

`pulseaudio --start`

- Kill the running pulseaudio daemon:

`pulseaudio --kill`

- List available modules:

`pulseaudio --dump-modules`

- Load a module into the currently running daemon with the specified arguments:

`pulseaudio --load="{{module_name}} {{arguments}}"`
