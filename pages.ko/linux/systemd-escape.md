# systemd-escape

> systemd 유닛 이름에서 사용할 문자열을 이스케이프합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-escape.html>.

- 주어진 텍스트 이스케이프:

`systemd-escape {{텍스트}}`

- 이스케이프 처리 역전:

`systemd-escape --unescape {{텍스트}}`

- 주어진 텍스트를 경로로 처리:

`systemd-escape --path {{텍스트}}`

- 이스케이프된 텍스트에 주어진 접미사 추가:

`systemd-escape --suffix {{접미사}} {{텍스트}}`

- 템플릿을 사용하여 이스케이프된 텍스트 삽입:

`systemd-escape --template {{템플릿}} {{텍스트}}`
