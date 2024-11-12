# systemd-inhibit

> 특정 전원 상태로의 진입을 금지.
> 인히비터 잠금을 사용하여 시스템의 절전 및 종료 요청을 차단하거나 지연시키고 자동 유휴 처리를 방지할 수 있습니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-inhibit.html>.

- 활성화된 모든 인히비션 잠금과 생성 이유 나열:

`systemd-inhibit --list`

- 지정된 초 동안 `sleep` 명령으로 시스템 종료 차단:

`systemd-inhibit --what shutdown sleep {{5}}`

- 다운로드가 완료될 때까지 시스템이 절전 또는 유휴 상태로 가지 않도록 유지:

`systemd-inhibit --what sleep:idle wget {{https://example.com/file}}`

- 스크립트가 종료될 때까지 노트북 덮개 닫힘 스위치 무시:

`systemd-inhibit --what sleep:handle-lid-switch {{경로/대상/스크립트}}`

- 명령이 실행되는 동안 전원 버튼 누름 무시:

`systemd-inhibit --what handle-power-key {{명령}}`

- 누가, 왜 인히비터를 생성했는지 설명 (기본값: `--who`의 경우 명령과 인수, `--why`의 경우 '알 수 없는 이유'):

`systemd-inhibit --who {{$USER}} --why {{이유}} --what {{작업}} {{명령}}`
