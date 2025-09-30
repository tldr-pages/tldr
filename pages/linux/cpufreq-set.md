# cpufreq-set

> A tool to modify CPU frequency settings.
> The frequency value should range between the output of command `cpufreq-info -l`.
> More information: <https://manned.org/cpufreq-set>.

- Set the CPU frequency policy of CPU 1 to "userspace":

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-g|--governor]}} {{userspace}}`

- Set the current minimum CPU frequency of CPU 1:

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-d|--min]}} {{min_frequency}}`

- Set the current maximum CPU frequency of CPU 1:

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-u|--max]}} {{max_frequency}}`

- Set the current work frequency of CPU 1:

`sudo cpufreq-set {{[-c|--cpu]}} {{1}} {{[-f|--freq]}} {{work_frequency}}`
