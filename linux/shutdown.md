# shutdown

> Shutdown and reboot the system

- Power off (halt) immediately

`shutdown -h now`

- Reboot immediately

`shutdown -r now`

- Reboot in 5 minutes

`shutdown -r +{{5}} &`

- Cancel a pending shutdown/reboot operation

`shutdown -c`
