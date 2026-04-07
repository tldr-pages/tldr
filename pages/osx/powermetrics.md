# powermetrics

> Display CPU usage, power consumption, and other system metrics on macOS.
> Useful for monitoring energy efficiency and performance of processes.
> More information: <https://www.unix.com/man_page/osx/1/powermetrics/>.

- Display power metrics with default settings (requires `sudo`):

`sudo powermetrics`

- Sample every 1000 milliseconds (1 second):

`sudo powermetrics --sample-rate {{1000}}`

- Take a specific number of samples and exit:

`sudo powermetrics --sample-count {{5}}`

- Show per-process energy impact:

`sudo powermetrics --show-process-energy`

- Output in plist format for machine parsing:

`sudo powermetrics --format plist`

- Save output to a file:

`sudo powermetrics --output-file {{path/to/file.txt}}`

- Use specific samplers (e.g., cpu_power, gpu_power):

`sudo powermetrics --samplers {{cpu_power,gpu_power}}`

- Display all available information:

`sudo powermetrics --show-all`
