# rpicam-raw

> Raspberry Pi 카메라에서 raw 비디오를 캡처합니다.
> 더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-raw>.

- 특정 초 동안 비디오 캡처:

`rpicam-raw -t {{2000}} -o {{경로/대상/파일.raw}}`

- 비디오 크기 및 프레임 속도 변경:

`rpicam-raw -t {{5000}} --width {{4056}} --height {{3040}} -o {{경로/대상/파일.raw}} --framerate {{8}}`
