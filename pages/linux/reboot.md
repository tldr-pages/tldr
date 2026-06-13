# reboot

> Reboot the system.
> More information: <https://manned.org/reboot.8>.

- Reboot the system:

`reboot`

- Power off the system (same as `poweroff`):

`reboot {{[-p|--poweroff]}}`

- Halt (terminates all processes and shuts down the CPU) the system (same as `halt`):

`reboot --halt`

- Reboot immediately without contacting the system manager:

`reboot {{[-f|--force]}}`

- Write the wtmp shutdown entry without rebooting the system:

`reboot {{[-w|--wtmp-only]}}`
