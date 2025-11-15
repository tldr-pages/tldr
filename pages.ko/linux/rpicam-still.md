# rpicam-still

> Raspberry Pi 카메라를 사용하여 사진을 촬영하고 저장하며, `rpicam-jpeg`에서 누락된 레거시 기능을 포함합니다.
> 더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-still>.

- 다른 인코딩 방식으로 사진 촬영:

`rpicam-still {{[-e|--encoding]}} {{bmp|png|rgb|yuv420}} {{[-o|--output]}} {{경로/대상/파일.[bmp|png|rgb|yuv420]}}`

- RAW 이미지 촬영:

`rpicam-still {{[-r|--raw]}} {{[-o|--output]}} {{경로/대상/파일.jpg}}`

- 100초 노출 이미지 촬영:

`rpicam-still {{[-o|--output]}} {{경로/대상/파일.jpg}} --shutter 100000`
