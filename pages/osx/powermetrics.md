# powermetrics

> Gather and display CPU usage, power, and interrupt wakeup statistics on macOS.
> Requires root privileges to run.
> More information: <https://www.unix.com/man_page/osx/1/powermetrics/>.

- Display CPU, power, and wakeup metrics using the default 5-second sample interval:

`sudo powermetrics`

- Sample metrics every 2 seconds indefinitely:

`sudo powermetrics --sample-interval {{2000}}`

- Take a specific number of samples then exit:

`sudo powermetrics --sample-count {{10}}`

- Save output to a file instead of `stdout`:

`sudo powermetrics --output-file {{path/to/output.txt}}`

- Order the process list by CPU time consumed:

`sudo powermetrics --order {{cputime}}`

- Display output in machine-readable plist format and print a usage summary on exit:

`sudo powermetrics --format {{plist}} --show-usage-summary`
