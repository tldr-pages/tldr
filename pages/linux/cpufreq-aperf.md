# cpufreq-aperf

> Calculate the average CPU frequency over a time period.
> Requires root privileges.

- Start calculating, default for all CPU cores and 1 second refresh interval:

`sudo cpufreq-aperf`

- Start calculating for CPU 1 only and 3 seconds refresh interval:

`sudo cpufreq-aperf -c {{1}} -i {{3}}`
