# microcom

> Egy minimalista terminálprogram, amely a konzolról soros, CAN vagy telnet kapcsolaton keresztül távoli eszközök elérésére szolgál. További információ: <https://manned.org/microcom>.

- Soros port megnyitása a megadott baud-ráta használatával:

`microcom --port {{path/to/serial_port}} --speed {{baud_rate}}`

- Telnet-kapcsolat létesítése a megadott állomáshoz:

`microcom --telnet {{hostname}}:{{port}}`
