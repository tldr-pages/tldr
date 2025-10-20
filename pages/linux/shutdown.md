# shutdown

> Shutdown and reboot the system.
> More information: <https://manned.org/shutdown.8>.

- Power off ([h]alt) immediately:

`shutdown -h now`

- Reboot immediately:

`shutdown {{[-r|--reboot]}} now`

- Reboot in 5 minutes:

`shutdown {{[-r|--reboot]}} +{{5}} &`

- Shutdown at 1:00 pm (Uses 24h clock):

`shutdown -h 13:00`

- [c]ancel a pending shutdown/reboot operation:

`shutdown -c`
