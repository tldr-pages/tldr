# f3probe

> Probe a block device (e.g. a flash drive or a microSD card) for counterfeit flash memory.
> See also `f3read`, `f3write`, `f3fix`.
> More information: <https://github.com/AltraMayor/f3>.

- Probe a block device:

`f3probe {{path/to/block_device}}`

- Use the minimum about of RAM possible:

`f3probe --min-memory {{path/to/block_device}}`

- Time disk operations:

`f3probe --time-ops {{path/to/block_device}}`
