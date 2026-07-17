# screenrecord

> 모바일 화면을 동영상으로 녹화.
> 참고: 이 명령은 `adb shell`을 통해서만 사용할 수 있음.
> 더 많은 정보: <https://developer.android.com/tools/adb#screenrecord>.

- 화면 녹화:

`screenrecord {{경로/대상/파일}}.mp4`

- 특정 해상도로 화면 녹화:

`screenrecord --size {{1280x720}} {{경로/대상/파일}}.mp4`

- 특정 비트레이트로 화면 녹화:

`screenrecord --bit-rate {{6000000}} {{경로/대상/파일}}.mp4`

- 최대 녹화 시간을 지정하여 화면 녹화 (최대 180초):

`screenrecord --time-limit {{180}} {{경로/대상/파일}}.mp4`

- 도움말 표시:

`screenrecord --help`
