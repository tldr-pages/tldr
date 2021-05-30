# chcpu

> Enable/disable a system's CPUs.
> More information: <https://github.com/karelzak/util-linux>.

- Disable CPUs via a list of CPU ID numbers:

`chcpu -d {{1,3}}`

- Enable a set of CPUs via a range of CPU ID numbers:

`chcpu -e {{1-10}}`
