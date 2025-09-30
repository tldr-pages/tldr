# pw-metadata

> PipeWire 객체의 메타데이터를 모니터링, 설정 및 삭제.
> 같이 보기: `pipewire`, `pw-mon`, `pw-cli`.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- `default` 이름의 메타데이터 표시:

`pw-metadata`

- `settings`에서 ID 0의 메타데이터 표시:

`pw-metadata {{[-n|--name]}} {{settings}} {{0}}`

- 사용 가능한 모든 메타데이터 객체 나열:

`pw-metadata {{[-l|--list]}}`

- 실행을 유지하며 메타데이터 변경 사항 기록:

`pw-metadata {{[-m|--monitor]}}`

- 모든 메타데이터 삭제:

`pw-metadata {{[-d|--delete]}}`

- `settings`에서 `log.level`을 1로 설정:

`pw-metadata {{[-n|--name]}} {{settings}} {{0}} {{log.level}} {{1}}`

- 도움말 표시:

`pw-metadata {{[-h|--help]}}`
