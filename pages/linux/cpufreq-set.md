# cpufreq-set

> A tool to modify CPU frequency settings.
> Requires root privileges.

- Set the CPU frequency policy of CPU 1 to "userspace":

`sudo cpufreq-set -c {{1}} -g {{userspace}}`

- Set the current minimum CPU frequency of CPU 1, value range between the output of command `cpufreq-info -l`:

`sudo cpufreq-set -c {{1}} --min {{min_frequency}}`

- Set the current maximum CPU frequency of CPU 1, value range between the output of command `cpufreq-info -l`:

`sudo cpufreq-set -c {{1}} --max {{max_frequency}}`

- Set the current work frequency of CPU 1 , value range between the output of command `cpufreq-info -l` (requires "userspace" policy to be loaded):

`sudo cpufreq-set -c {{1}} -f {{work_frequency}}`
