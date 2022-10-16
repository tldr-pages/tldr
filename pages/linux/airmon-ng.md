# airmon-ng

> Turn wireless cards into monitor mode.
> More information: <https://www.aircrack-ng.org/doku.php#documentation>.

- List all possible programs that could interference with the wireless card and stop all of them.

`sudo airmon-ng check kill`

- Enable monitor mode on an interface.

`sudo airmon-ng start {{ interface }}`

- Disable monitor mode on an interface and go back to managed mode.

`sudo airmon-ng stop {{ interface }}`
