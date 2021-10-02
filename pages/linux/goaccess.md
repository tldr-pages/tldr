# goaccess

> GoAccess is an open source real-time web log analyzer.
> More information: <https://goaccess.io>.

- Run `goaccess` in interactive mode:

`goaccess {{path/to/file}} [{{path/to/file}}]`

- Use a specific log-format (or pre-defined formats like **combined**):

`goaccess {{path/to/file}} --log-format={{format}}`

- Trace a logfile and pipe it to `goaccess`:

`tail -f {{path/to/logfile}} | goaccess -`

- Realtime HTML output in a single file (you can even mail this):

`goaccess {{path/to/file}} --output {{path/to/file}} --real-time-html`
