# caffeinate

> Prevent desktop from sleeping.
> More information: <https://manned.org/caffeinate>.

- Prevent from sleeping for 1 hour (3600 seconds):

`caffeinate -u -t {{3600}}`

- Prevent from sleeping until a command completes:

`caffeinate -s "{{command}}"`

- Prevent from sleeping until you type Ctrl-C:

`caffeinate -i`
