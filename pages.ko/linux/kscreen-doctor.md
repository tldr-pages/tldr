# kscreen-doctor

> 화면 설정을 변경하고 조작합니다.
> 더 많은 정보: <https://invent.kde.org/plasma/libkscreen>.

- 디스플레이 출력 정보 표시:

`kscreen-doctor --outputs`

- ID가 1인 디스플레이 출력의 회전을 오른쪽으로 설정:

`kscreen-doctor {{output.1.rotation.right}}`

- ID가 `HDMI-2`인 디스플레이 출력의 배율을 2 (200%)로 설정:

`kscreen-doctor {{output.HDMI-2.scale.2}}`
