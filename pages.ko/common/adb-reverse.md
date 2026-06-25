# adb reverse

> Android 기기 또는 에뮬레이터에서 소켓 연결을 역방향으로 포워딩.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터 및 기기의 모든 역방향 소켓 연결 목록 출력:

`adb reverse --list`

- 단일로 연결된 에뮬레이터 또는 기기에서 localhost로 TCP 포트 역방향 포워딩:

`adb reverse tcp:{{원격_포트}} tcp:{{로컬_포트}}`

- 특정 에뮬레이터 또는 기기 (디바이스 ID / 시리얼([s]erial) 번호)에서 localhost로 TCP 포트 역방향 포워딩:

`adb -s {{device_id}} reverse tcp:{{원격_포트}} tcp:{{로컬_포트}}`

- 에뮬레이터 또는 기기에서 역방향 소켓 연결 제거:

`adb reverse --remove tcp:{{원격_포트}}`

- 모든 에뮬레이터 및 기기의 역방향 소켓 연결 제거:

`adb reverse --remove-all`
