# cpufreq-info

> Show CPU frequency information.
> More information: <https://manned.org/cpufreq-info>.

- Show CPU frequency information for all CPUs:

`cpufreq-info`

- Show CPU frequency information for the specified CPU:

`cpufreq-info {{[-c|--cpu]}} {{cpu_number}}`

- Show the allowed minimum and maximum CPU frequency:

`cpufreq-info {{[-l|--hwlimits]}}`

- Show the current minimum and maximum CPU frequency and policy in table format:

`cpufreq-info {{[-o|--proc]}}`

- Show available CPU frequency policies:

`cpufreq-info {{[-g|--governors]}}`

- Show current CPU work frequency in a human-readable format, according to the cpufreq kernel module:

`cpufreq-info {{[-f|--freq]}} {{[-m|--human]}}`

- Show current CPU work frequency in a human-readable format, by reading it from hardware (only available to root):

`sudo cpufreq-info {{[-w|--hwfreq]}} {{[-m|--human]}}`
