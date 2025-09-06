# esptool.py

> Espressif 칩용 부트로더 유틸리티 (예: ESP8266).
> 더 많은 정보: <https://docs.espressif.com/projects/esptool/en/latest/esp32/>.

- 특정 포트 및 전송 속도를 사용하여 펌웨어 파일을 ESP 칩에 플래시:

`sudo esptool.py --port {{포트}} --baud {{전송_속도}} write_flash 0x0 {{경로/대상/펌웨어.bin}}`

- ESP 칩의 플래시를 지움:

`sudo esptool.py --port {{포트}} --baud {{전송_속도}} erase_flash`
