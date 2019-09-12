# nnn

> Interactive terminal file manager and disk usage analyzer.
> More information: <https://github.com/jarun/nnn>.

- Open the current directory (or specify one as the first argument):

`nnn`

- Open an existing bookmark (defined in the `NNN_BMS` environment variable):

`nnn -b {{bookmark_name}}`

- Show hidden files:

`nnn -d`

- Start in disk usage analyzer mode:

`nnn -S`

- Start in light mode (fewer details):

`nnn -l`

- Copy the selected file path to a specific output file (stdout if output file is `-`):

`nnn -p {{path/to/output_file}}`

- Use substring matching for filters instead of regex:

`nnn -s`

- Use version compare to sort files:

`nnn -n`
