# rpicam-jpeg

> Raspberry Pi 카메라를 사용하여 JPEG 이미지를 캡처하고 저장.
> 더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-jpeg>.

- 이미지를 캡처하고 파일명 지정:

`rpicam-jpeg -o {{경로/대상/파일.jpg}}`

- 설정된 크기로 이미지 캡처:

`rpicam-jpeg -o {{경로/대상/파일.jpg}} --width {{1920}} --height {{1080}}`

- 20초의 노출과 150%의 게인으로 이미지 캡처:

`rpicam-jpeg -o {{경로/대상/파일.jpg}} --shutter 20000 --gain 1.5`
