# esptool.py

> Espressif 芯片（例如 ESP8266）的引导加载程序工具。
> 更多信息：<https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- 将固件文件闪存到具有给定端口和波特率的 ESP 芯片：

`sudo esptool.py --port {{port}} --baud {{baud_rate}} write_flash 0x0 {{path/to/firmware.bin}}`

- 清除 ESP 芯片的闪存：

`sudo esptool.py --port {{port}} --baud {{baud_rate}} erase_flash`