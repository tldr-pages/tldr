# v4l2-ctl

> 비디오 장치 제어.
> 더 많은 정보: <https://manned.org/v4l2-ctl>.

- 모든 비디오 장치 나열:

`v4l2-ctl --list-devices`

- 기본 비디오 장치 `/dev/video0`의 지원 비디오 포맷과 해상도 나열:

`v4l2-ctl --list-formats-ext`

- 특정 비디오 장치의 지원 비디오 포맷과 해상도 나열:

`v4l2-ctl --list-formats-ext {{[-d|--device]}} {{경로/대상/비디오_장치}}`

- 비디오 장치의 모든 세부 정보 가져오기:

`v4l2-ctl --all {{[-d|--device]}} {{경로/대상/비디오_장치}}`

- 특정 해상도로 비디오 장치에서 JPEG 사진 캡처:

`v4l2-ctl {{[-d|--device]}} {{경로/대상/비디오_장치}} --set-fmt-video=width={{너비}},height={{높이}},pixelformat=MJPG --stream-mmap --stream-to={{경로/대상/출력.jpg}} --stream-count=1`

- 비디오 장치에서 원시 비디오 스트림 캡처:

`v4l2-ctl {{[-d|--device]}} {{경로/대상/비디오_장치}} --set-fmt-video=width={{너비}},height={{높이}},pixelformat={{포맷}} --stream-mmap --stream-to={{경로/대상/출력}} --stream-count={{캡처할_프레임_수}}`

- 모든 비디오 장치의 컨트롤과 그 값 나열:

`v4l2-ctl {{[-l|--list-ctrls]}} {{[-d|--device]}} {{경로/대상/비디오_장치}}`

- 비디오 장치 컨트롤 값 설정:

`v4l2-ctl {{[-d|--device]}} {{경로/대상/비디오_장치}} {{[-c|--set-ctrl]}} {{컨트롤_이름}}={{값}}`
