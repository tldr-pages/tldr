# cpufreq-info

> A tool to show CPU frequency information.

- Show CPU frequency kernel information for all CPUs:

`cpufreq-info`

- Show CPU frequency kernel information for the specified CPU:

`cpufreq-info -c {{cpu_number}}`

- Show current CPU work frequency in a human-readable format, according to the kernel module:

`cpufreq-info -f -m`

- Show current CPU work frequency in a human-readable format, by reading it from hardware (only available to root):

`sudo cpufreq-info -w -m`

- Show the minimum and maximum CPU frequency allowed:

`cpufreq-info -l`

- Show the currently used CPU frequency policy:

`cpufreq-info -p`

- Show available CPU frequency policies:

`cpufreq-info -g`

- Show the minimum, maximum CPU frequency and currently used policy in table format:

`cpufreq-info -o`
