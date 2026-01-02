# halt

> Halt the system.
> More information: <https://manned.org/halt>.

- Halt the system:

`halt`

- Power off the system (same as `poweroff`):

`halt {{[-p|--poweroff]}}`

- Reboot the system (same as `reboot`):

`halt --reboot`

- Halt immediately without contacting the system manager:

`halt {{[-f|--force]}}`

- Write the wtmp shutdown entry without halting the system:

`halt {{[-w|--wtmp-only]}}`
