# powermetrics

> Gather and display CPU usage, power, and interrupt wakeup statistics.
> More information: <https://keith.github.io/xcode-man-pages/powermetrics.1.html>.

- Display CPU, power, and wakeup metrics using the default 5-second sample interval:

`sudo powermetrics`

- Sample metrics every 2000 milliseconds taking 10 samples then exit:

`sudo powermetrics {{[-i|--sample-rate]}} 2000 {{[-n|--sample-count]}} 10`

- Save output to a file instead of `stdout`:

`sudo powermetrics {{[-o|--output-file]}} {{path/to/output.txt}}`

- Order the process list by the specified method (default: `composite`):

`sudo powermetrics {{[-r|--order]}} {{pid|wakeups|cputime|composite}}`

- Display output in machine-readable property list format and print a usage summary on exit:

`sudo powermetrics {{[-f|--format]}} plist --show-usage-summary`
