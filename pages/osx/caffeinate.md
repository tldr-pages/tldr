# caffeinate

> Prevent macOS from sleeping.
> More information: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Prevent from sleeping for 1 hour (3600 seconds):

`caffeinate -u -t {{3600}}`

- Prevent from sleeping until a command completes:

`caffeinate -s "{{command}}"`

- Prevent from sleeping until a process with the specified PID completes:

`caffeinate -w {{pid}}`

- Prevent from sleeping (use `Ctrl + C` to exit):

`caffeinate -i`

- Prevent disk from sleeping (use `Ctrl + C` to exit):

`caffeinate -m`
