# powermetrics

> Gather and display CPU usage, power, and interrupt wakeup statistics.
> More information: <https://keith.github.io/xcode-man-pages/powermetrics.1.html>.

- Display CPU, power, and wakeup metrics using the default 5-second sample interval:

`sudo powermetrics`

- Sample metrics every 2 seconds, taking 10 samples then exit:

`sudo powermetrics --sample-interval {{2000}} --sample-count {{10}}`

- Save output to a file instead of `stdout`:

`sudo powermetrics --output-file {{path/to/output.txt}}`

- Order the process list by a specified method (`pid`, `wakeups`, `cputime`, or `composite`):

`sudo powermetrics --order {{composite}}`

- Display output in machine-readable plist format and print a usage summary on exit:

`sudo powermetrics --format {{plist}} --show-usage-summary`
