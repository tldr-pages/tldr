# goaccess

> GoAccess is an open source real-time web log analyzer.
> More information: <https://goaccess.io>.

- Interactive mode:

`goaccess {{path/to/logfile}} [{{another/log/logfile}}]`

- Use a specific log-format (or pre-defined formats like **combined**):

`goaccess {{path/to/logfile}} --log-format={{format}}`

- Trace a logfile and pipe it to goacces:

`tail -f {{path/to/logfile}} | goaccess -`

- Realtime HTML output in a single file (you can even mail this):

`goaccess {{path/to/logfile}} --output {{path/to/html-file}} --real-time-html`
