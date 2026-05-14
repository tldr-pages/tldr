# dnf changelog

> 지정한 패키지의 변경 로그 조회.
> 기본 `dnf` 명령에는 포함되지 않으며, `dnf-plugins-core`을 통해 지원됨.
> 관련 항목: `dnf`.
> 더 많은 정보: <https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html>.

- 지정한 패키지의 모든 변경 로그 표시:

`dnf changelog {{패키지}}`

- 지정한 날짜 이후의 변경 로그만 표시:

`dnf changelog --since {{날짜}} {{패키지}}`

- 지정한 패키지의 최근 `n`개의 변경 로그만 표시:

`dnf changelog --count {{숫자}} {{패키지}}`

- 업그레이드 가능한 패키지의 새로운 변경 항목만 표시:

`dnf changelog --upgrades {{패키지}}`

- 도움말 표시:

`dnf changelog --help-cmd`
