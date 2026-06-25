# screencap

> 모바일 디스플레이의 스크린샷 찍기.
> 참고: 이 명령은 `adb shell`을 통해서만 사용할 수 있습니다.
> 더 많은 정보: <https://developer.android.com/tools/adb#screencap>.

- 스크린샷 찍기:

`screencap {{경로/대상/파일}}`

- 화면을 캡처해 PNG 형식으로 표준 출력(`stdout`)에 표시:

`screencap -p`

- `adb` 연결 통해 화면을 캡처하고 로컬 파일로 저장:

`adb shell screencap -p > {{경로/대상/이미지.png}}`

- 도움말 표시:

`screencap -h`
