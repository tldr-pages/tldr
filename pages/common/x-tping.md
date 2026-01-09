# x tping

> Ping TCP port.
> This module leverages the TCP protocol and utilizes curl to establish a straightforward, plain-text TCP connection from your local machine to the target host and port.
> More information: <https://x-cmd.com/mod/tping>.

- Ping a host on default port 80 with verbose mode:

`x tping {{host}}`

- Ping a host with specific port:

`x tping {{host}}:{{port}}`

- Show results as a heatmap:

`x tping --heatmap {{host}}`

- Show results as a bar graph:

`x tping --bar {{host}}:{{port}}`

- Output in raw data mode:

`x tping --raw {{host}}`

- Output in CSV format:

`x tping --csv {{host}}`

- Output in TSV format:

`x tping --tsv {{host}}`

- Send a TCP connection (run subcommand):

`x tping run {{host}}:{{port}}`