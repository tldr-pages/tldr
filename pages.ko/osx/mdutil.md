# mdutil

> Spotlight의 색인을 위한 메타데이터 저장소 관리 도구.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/mdutil.1.html>.

- 시작 볼륨의 색인 상태 표시:

`mdutil -s {{/}}`

- 특정 볼륨의 Spotlight 색인 기능 켜기/끄기:

`mdutil -i {{on|off}} {{경로/대상/볼륨}}`

- 모든 볼륨의 색인 기능 켜기/끄기:

`mdutil -a -i {{on|off}}`

- 메타데이터 저장소를 지우고 색인 프로세스 재시작:

`mdutil -E {{경로/대상/볼륨}}`
