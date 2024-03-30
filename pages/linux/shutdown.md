# shutdown

> Shutdown and reboot the system.
> More information: <https://manned.org/shutdown.8>.

- Power off ([h]alt) immediately:

`shutdown -h now`

- [r]eboot immediately:

`shutdown -r now`

- [r]eboot in 5 minutes:

`shutdown -r +{{5}} &`

- Shutdown at 1:00 pm (Uses 24[h] clock):

`shutdown -h 13:00`

- [c]ancel a pending shutdown/reboot operation:

`shutdown -c`
