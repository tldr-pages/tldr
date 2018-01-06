# cpufreq-set

> A tool to modify CPU frequency settings.
> Requires root privileges.

- Set the CPU frequency policy of CPU 1 to "userspace":

`sudo cpufreq-set -c {{1}} -g {{userspace}}`

- Set the minimum CPU frequency of CPU 1:

`sudo cpufreq-set -c {{1}} --min {{min_frequency}}`

- Set the maximum CPU frequency of CPU 1:

`sudo cpufreq-set -c {{1}} --max {{max_frequency}}`

- Set the work frequency of CPU 1 (requires "userspace" policy to be loaded):

`sudo cpufreq-set -c {{1}} -f {{work_frequency}}`
