# screencapture

> 스크린샷과 화면 녹화를 위한 유틸리티.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/screencapture.1.html>.

- 스크린샷을 찍어 파일로 저장:

`screencapture {{경로/대상/파일.png}}`

- 마우스 커서를 포함하여 스크린샷 찍기:

`screencapture -C {{경로/대상/파일.png}}`

- 스크린샷을 찍고 저장하는 대신 미리보기로 열기:

`screencapture -P`

- 선택한 직사각형 영역의 스크린샷 찍기:

`screencapture -i {{경로/대상/파일.png}}`

- 지연 후 스크린샷 찍기:

`screencapture -T {{초}} {{경로/대상/파일.png}}`

- 화면 녹화를 하고 파일로 저장:

`screencapture -v {{경로/대상/파일.mp4}}`
