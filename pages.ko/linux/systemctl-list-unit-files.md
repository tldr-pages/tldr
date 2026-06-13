# systemctl list-unit-files

> 설치된 유닛 파일과 활성화 상태를 나열.
> 관련 항목: `systemctl list-units`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-unit-files%20PATTERN%E2%80%A6>.

- 설치된 유닛 파일과 상태 출력:

`systemctl list-unit-files`

- 상태를 기준으로 필터링:

`systemctl list-unit-files --state {{enabled|disabled|static|...}}`

- 유닛 타입 기준으로 필터링:

`systemctl list-unit-files {{[-t|--type]}} {{service|socket|timer|...}}`

- 이름 기준으로 필터링:

`systemctl list-unit-files '{{sshd*}}'`

- 출력을 페이저 없이 `stdout`로 출력:

`systemctl list-unit-files --no-pager`

- 헤더 및 푸터 제외 출력:

`systemctl list-unit-files --no-legend`
