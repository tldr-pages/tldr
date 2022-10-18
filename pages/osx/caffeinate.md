# caffeinate

> Prevent macOS from sleeping.
> More information: <https://ss64.com/osx/caffeinate.html>.

- Prevent from sleeping for `x` seconds:

`caffeinate -u -t {{x}}`

- Prevent from sleeping until a command completes:

`caffeinate -s "{{command}}"`

- Prevent from sleeping until you type Ctrl-C:

`caffeinate -i`
