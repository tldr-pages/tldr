# cpupower

> Tools regarding CPU power and tuning options.
> This command is available as part of the `cpupower` package, or on Fedora as part of `kernel-tools`.
> More information: <https://manned.org/cpupower>.

- List CPUs:

`sudo cpupower --cpu cpulist`

- Print information about all cores:

`sudo cpupower --cpu {{all}} info`

- Set all CPUs to a power-saving frequency governor:

`sudo cpupower --cpu {{all}} frequency-set --governor {{powersave}}`

- Print CPU 0's available frequency [g]overnors:

`sudo cpupower --cpu {{0}} frequency-info g | grep "analyzing\|governors"`

- Print CPU 4's frequency from the hardware, in a human-readable format:

`sudo cpupower --cpu {{4}} frequency-info --hwfreq --human`
