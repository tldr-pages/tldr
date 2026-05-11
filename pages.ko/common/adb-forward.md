# adb forward

> Android 기기 또는 에뮬레이터로 소켓 연결을 포워딩.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 단일로 연결된 에뮬레이터 또는 기기로 TCP 포트 포워딩:

`adb forward tcp:{{로컬_포트}} tcp:{{원격_포트}}`

- 특정 에뮬레이터 또는 기기(디바이스 ID / 시리얼([s]erial) 번호)를 대상으로 TCP 포트 포워딩:

`adb -s {{장치_id}} forward tcp:{{로컬_포트}} tcp:{{원격_포트}}`

- 모든 포워딩 목록 출력:

`adb forward --list`

- 특정 포워딩 규칙 제거:

`adb forward --remove tcp:{{로컬_포트}}`

- 모든 포워딩 규칙 제거:

`adb forward --remove-all`
