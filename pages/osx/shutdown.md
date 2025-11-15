# shutdown

> Shutdown and reboot the system.
> More information: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

- Power off (halt) immediately:

`shutdown -h now`

- Sleep immediately:

`shutdown -s now`

- Reboot immediately:

`shutdown -r now`

- Reboot in 5 minutes:

`shutdown -r "+{{5}}"`

- Power off (halt) at 1:00 pm (Uses 24h clock):

`shutdown -h {{1300}}`

- Reboot on May 10th 2042 at 11:30 am (Input format: YYMMDDHHMM):

`shutdown -r {{4205101130}}`
