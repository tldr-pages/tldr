# esptool.py

> Bootloader utility for Espressif chips (e.g. ESP8266).
> More information: <https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- Flash a firmware file to an ESP chip with a given port and baud rate:

`sudo esptool.py --port {{port}} --baud {{baud_rate}} write_flash 0x0 {{path/to/firmware.bin}}`

- Clear the flash of an ESP chip:

`sudo esptool.py --port {{port}} --baud {{baud_rate}} erase_flash`
