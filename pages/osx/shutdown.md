# shutdown

> Shutdown and reboot the system.

- Power off (halt) immediately:

`shutdown -h now`

- Sleep immediately:

`shutdown -s now`

- Reboot immediately:

`shutdown -r now`

- Reboot in 5 minutes:

`shutdown -r +{{5}}`

- Power off (halt) today at 23:00

`shutdown -h {{2300}}`

- Reboot on May 10th 2042 at 11:30

`shutdown -r {{4205101130}}`
