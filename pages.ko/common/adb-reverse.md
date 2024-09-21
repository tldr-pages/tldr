# adb reverse

> 안드로이드 디버그 브릿지 역방향: 안드로이드 에뮬레이터 인스턴스 또는 연결된 안드로이드 장치에서 소켓 연결을 역방향으로 수행
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 에뮬레이터 및 장치의 모든 역방향 소켓 연결을 나열:

`adb reverse --list`

- 에뮬레이터 또는 장치의 TCP 포트를 localhost로 전환:

`adb reverse tcp:{{원격_포트}} tcp:{{로컬_포트}}`

- 에뮬레이터 또는 장치에서 역방향 소켓 연결을 제거:

`adb reverse --remove tcp:{{원격_포트}}`

- 모든 에뮬레이터 또는 장치에서 역방향 소켓 연결을 제거:

`adb reverse --remove-all`
