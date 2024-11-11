# rpicam-hello

> Raspberry Pi 카메라를 사용하여 실시간 카메라 스트림 보기.
> 더 많은 정보: <https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-hello>.

- 특정 시간(밀리초) 동안 카메라 미리보기 스트림 표시:

`rpicam-hello -t {{시간}}`

- 특정 카메라 센서를 위한 설정 조정:

`rpicam-hello --tuning-file {{/usr/share/libcamera/ipa/rpi/경로/대상/config.json}}`
