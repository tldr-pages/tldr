# esptool.py

> Bootloader օգտակար Espressif չիպերի համար (օրինակ՝ ESP8266):.
> Լրացուցիչ տեղեկություններ. <https://docs.espressif.com/projects/esptool/en/latest/esp32/>:.

- Ֆլեշ ծրագրաշարի ֆայլը ESP չիպի վրա՝ տվյալ պորտով և բուդի արագությամբ.:

`sudo esptool.py --port {{port}} --baud {{baud_rate}} write_flash 0x0 {{path/to/firmware.bin}}`

- Մաքրել ESP չիպի բռնկումը.:

`sudo esptool.py --port {{port}} --baud {{baud_rate}} erase_flash`
