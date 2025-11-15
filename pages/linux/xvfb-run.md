# xvfb-run

> Run a command in a virtual X server environment.
> More information: <https://manned.org/xvfb-run>.

- Run the specified command in a virtual X server:

`xvfb-run {{command}}`

- Try to get a free server number, if the default (99) is not available:

`xvfb-run {{[-a|--auto-servernum]}} {{command}}`

- Pass arguments to the Xvfb server:

`xvfb-run {{[-s|--server-args]}} "{{-screen 0 1024x768x24}}" {{command}}`
