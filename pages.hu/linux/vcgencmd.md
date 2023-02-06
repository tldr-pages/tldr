# vcgencmd

> Rendszerinformációk nyomtatása egy Raspberry Pi számára. További információ: <https://www.raspberrypi.org/documentation/computers/os.html#vcgencmd>.

- Az összes elérhető parancs listája:

`vcgencmd commands`

- A CPU aktuális hőmérsékletének kiírása:

`vcgencmd measure_temp`

- Az aktuális feszültség kiírása:

`vcgencmd measure_volts`

- A rendszer fojtott állapotának kiírása bitmintaként:

`vcgencmd get_throttled`

- A bootloader konfigurációjának nyomtatása (csak a Raspberry Pi 4 modellek esetében érhető el):

`vcgencmd bootloader_config`

- Súgó megjelenítése:

`vcgencmd --help`
