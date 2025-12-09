# pactl

> 실행 중인 PulseAudio 사운드 서버 제어.
> 더 많은 정보: <https://manned.org/pactl>.

- 사운드 서버 정보 표시:

`pactl info`

- 모든 싱크(또는 다른 유형 - 싱크는 출력이고 싱크 입력은 활성 오디오 스트림) 나열:

`pactl list {{sinks}} short`

- 기본 싱크(출력)를 1로 변경 (번호는 `list` 하위 명령을 통해 확인 가능):

`pactl set-default-sink {{1}}`

- 싱크 입력 627을 싱크 1로 이동:

`pactl move-sink-input {{627}} {{1}}`

- 싱크 1의 볼륨을 75%로 설정:

`pactl set-sink-volume {{1}} {{0.75}}`

- 기본 싱크의 음소거 전환 (특수 이름 `@DEFAULT_SINK@` 사용):

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`
