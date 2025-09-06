# systemd-path

> 시스템 및 사용자 경로를 나열하고 조회.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-path.html>.

- 알려진 경로와 현재 값을 나열:

`systemd-path`

- 지정된 경로를 조회하고 값을 표시:

`systemd-path "{{경로_이름}}"`

- 출력된 경로에 `{{suffix_string}}` 접미사를 추가:

`systemd-path --suffix {{suffix_string}}`

- 짧은 버전 문자열을 출력하고 종료:

`systemd-path --version`
