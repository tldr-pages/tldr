# goaccess

> An open source real-time web log analyzer.
> More information: <https://goaccess.io>.

- Analyze one or more log files in interactive mode:

`goaccess {{path/to/file}} [{{path/to/file}}]`

- Use a specific log-format (or pre-defined formats like "combined"):

`goaccess {{path/to/file}} --log-format={{format}}`

- Analyse a log from stdin:

`tail -f {{path/to/logfile}} | goaccess -`

- Analyze a log and write it to an HTML file in real-time:

`goaccess {{path/to/logfile}} --output {{path/to/file.html}} --real-time-html`
