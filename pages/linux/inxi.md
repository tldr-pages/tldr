# inxi

> Print a summary of system information and resources for debugging purposes.
> See also: `lshw`, `hwinfo`.
> More information: <https://manned.org/inxi>.

- Print a summary of CPU, memory, hard drive and kernel information:

`inxi`

- Print a full description of CPU, memory, disk, network, and process information and filter sensitive information:

`inxi {{[-ez|--expanded --filter]}}`

- Print a summary of CPU information:

`inxi {{[-C|--cpu]}}`

- Print a summary of graphics information:

`inxi {{[-G|--graphics]}}`

- Print a summary of system RAM:

`inxi {{[-m|--memory]}}`

- Print a summary of system audio:

`inxi {{[-A|--audio]}}`

- Print available sensor data:

`inxi {{[-s|--sensors]}}`

- Print information about the distribution's repositories:

`inxi {{[-r|--repos]}}`
