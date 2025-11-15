# emulator

> Android 에뮬레이터 관리.
> 더 많은 정보: <https://developer.android.com/studio/run/emulator-commandline>.

- Android 에뮬레이터 장치를 시작:

`emulator -avd {{이름}}`

- 에뮬레이션에 사용할 수 있는 개발 컴퓨터에 웹캠을 표시:

`emulator -avd {{이름}} -webcam-list`

- 후면 카메라 설정을 무시하고 에뮬레이터를 시작 (전면 카메라의 경우 `-camera-front` 사용):

`emulator -avd {{이름}} -camera-back {{none|emulated|webcamN}}`

- 최대 네트워크 속도로 에뮬레이터를 시작:

`emulator -avd {{이름}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- 네트워크 대기 시간이 있는 에뮬레이터를 시작:

`emulator -avd {{이름}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- 지정된 HTTP/HTTPS 프록시를 통해, 모든 TCP 연결을 만들어 에뮬레이터를 시작 (포트 번호가 필요함):

`emulator -avd {{이름}} -http-proxy {{http://example.com:80}}`

- 지정된 SD 카드 파티션 이미지 파일로 에뮬레이터를 시작:

`emulator -avd {{이름}} -sdcard {{경로/대상/sdcard.img}}`

- 도움말 표시:

`emulator -help`
