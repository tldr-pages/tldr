# pulseaudio

> The PulseAudio sound system daemon and manager.
> More information: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Check if PulseAudio is running (a non-zero exit code means it is not running):

`pulseaudio --check`

- Start the PulseAudio daemon in the background:

`pulseaudio --start`

- Kill the running PulseAudio daemon:

`pulseaudio --kill`

- List available modules:

`pulseaudio --dump-modules`

- Load a module into the currently running daemon with the specified arguments:

`pulseaudio --load="{{module_name}} {{arguments}}"`
