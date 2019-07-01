# cpufreq-aperf

> Calculate the average CPU frequency over a time period.
> Requires root privileges.

- Start calculating, defaulting to all CPU cores and 1 second refresh interval:

`sudo cpufreq-aperf`

- Start calculating for CPU 1 only:

`sudo cpufreq-aperf -c {{1}}`

- Start calculating with a 3 seconds refresh interval for all CPU cores:

`sudo cpufreq-aperf -i {{3}}`

- Calculate only once:

`sudo cpufreq-aperf -o`
