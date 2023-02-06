# esptool.py

> Bootloader segédprogram Espressif chipekhez (pl. ESP8266). További információ: <https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- Firmware fájl flashelése egy ESP chipre egy adott porttal és baud rátával:

`sudo esptool.py --port {{port}} --baud {{baud_rate}} write_flash 0x0 {{path/to/firmware.bin}}`

- Egy ESP-chip flashének törlése:

`sudo esptool.py --port {{port}} --baud {{baud_rate}} erase_flash`
