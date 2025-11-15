# rpi-imager

> 이미지를 저장 장치에 플래시.
> 더 많은 정보: <https://github.com/raspberrypi/rpi-imager>.

- 특정 이미지를 특정 블록 장치에 기록:

`rpi-imager --cli {{경로/대상/이미지.zip}} {{/dev/sdX}}`

- 체크섬 검증을 비활성화한 상태로 특정 이미지를 블록 장치에 기록:

`rpi-imager --cli --disable-verify {{경로/대상/이미지.zip}} {{/dev/sdX}}`

- 검증 시 특정 체크섬을 기대하는 상태로 특정 이미지를 블록 장치에 기록:

`rpi-imager --cli --sha256 {{기대_해시}} {{경로/대상/이미지.zip}} {{/dev/sdX}}`
