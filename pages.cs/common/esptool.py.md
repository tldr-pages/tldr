# esptool.py

> Bootloader nástroj pro Espressif čipy (např. ESP8266).
> Více informací: <https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- Flashnout firmware soubor do ESP čipu s uvedeným portem a přenosovou rychlostí:

`sudo esptool.py --port {{port}} --baud {{prenosova_rychlost}} write_flash 0x0 {{cesta/k/firmwaru.bin}}`

- Smazat flash ESP čipu:

`sudo esptool.py --port {{port}} --baud {{prenosova_rychlost}} erase_flash`
