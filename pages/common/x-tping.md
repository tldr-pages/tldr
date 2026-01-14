# x tping

> Ping a host via TCP to check reachability.
> More information: <https://x-cmd.com/mod/tping>.

- Ping a host on default port 80 with verbose mode:

`x tping {{host}}`

- Ping a host with specific port:

`x tping {{host}}:{{port}}`

- Show results as a heatmap:

`x tping {{[-m|--heatmap]}} {{host}}`

- Show results as a bar graph:

`x tping {{[-b|--bar]}} {{host}}:{{port}}`

- Output in raw data mode:

`x tping {{[-r|--raw]}} {{host}}`

- Output in a specific format:

`x tping {{--csv|--tsv}} {{host}}`
