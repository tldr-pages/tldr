# cpupower

> Tools regarding CPU power and tuning options.
> More information: <https://manned.org/cpupower>.

- List CPUs:

`sudo cpupower {{[-c|--cpu]}} {{all}} info`

- Print information about all cores:

`sudo cpupower {{[-c|--cpu]}} {{all}} info`

- Set all CPUs to a power-saving frequency governor:

`sudo cpupower {{[-c|--cpu]}} {{all}} frequency-set --governor {{powersave}}`

- Print CPU 0's available frequency governors:

`sudo cpupower {{[-c|--cpu]}} {{0}} frequency-info {{[-g|--governors]}} | grep "analyzing\|governors"`

- Print CPU 4's frequency from the hardware, in a human-readable format:

`sudo cpupower {{[-c|--cpu]}} {{4}} frequency-info {{[-w|--hwfreq]}} {{[-m|--human]}}`
