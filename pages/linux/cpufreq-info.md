# cpufreq-info

> A tool to show CPU frequency information.

- Show cpufreq kernel information for all CPUs:

`cpufreq-info`

- Show cpufreq kernel information for specified CPU:

`cpufreq-info -c {{cpu_number}}`

- Show current CPU work frequency in human-readable format, according to the cpufreq core:

`cpufreq-info -f -m`

- Show current CPU work frequency in human-readable format, by reading it from hardware (only available to root):

`sudo cpufreq-info -w -m`

- Show the minimum and maximum CPU frequency allowed:

`cpufreq-info -l`

- Show the currently used cpufreq policy:

`cpufreq-info -p`

- Show available cpufreq policy:

`cpufreq-info -g`

- Show the minimum, maximum CPU frequency and currently used cpufreq policy in table format:

`cpufreq-info -o`
