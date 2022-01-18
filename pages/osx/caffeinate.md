# caffeinate

> Prevent macOS from sleeping.
> There are no options to get help or version.
> More information: <https://ss64.com/osx/caffeinate.html>.

- Prevent from sleeping for 1 hour (3600 seconds):

`caffeinate -u -t {{3600}}`

- Prevent from sleeping until a command completes:

`caffeinate -s "{{command}}"`

- Prevent from sleeping until you type Ctrl-C:

`caffeinate -i`
