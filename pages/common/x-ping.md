# x ping

> Enhanced modules for ping.
> More information: <https://x-cmd.com/mod/ping>.

- Ping a specific host (defaults to bing.com if omitted):

`x ping {{host}}`

- Show ping results as a heatmap:

`x ping {{[-m|--heatmap]}} {{host}}`

- Show ping results as a bar graph:

`x ping {{[-b|--bar]}} {{host}}`

- Process ping results and display as heatmap:

`ping {{host}} | x ping vis {{[-m|--heatmap]}}`

- Show help:

`x ping {{[-h|--help]}}`
