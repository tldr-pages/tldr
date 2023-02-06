# minicom

> Egy program, amely egy eszköz soros interfészével kommunikál. További információ: <https://manned.org/minicom>.

- Egy adott soros port megnyitása:

`sudo minicom --device {{/dev/ttyUSB0}}`

- Egy adott soros port megnyitása adott baud-ráta mellett:

`sudo minicom --device {{/dev/ttyUSB0}} --baudrate {{115200}}`

- Belépés a konfigurációs menübe egy adott soros porttal való kommunikáció előtt:

`sudo minicom --device {{/dev/ttyUSB0}} --setup`
