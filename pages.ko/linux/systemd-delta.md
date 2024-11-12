# systemd-delta

> 재정의된 systemd 관련 설정 파일을 찾습니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-delta.html>.

- 모든 재정의된 설정 파일 표시:

`systemd-delta`

- 특정 유형의 파일만 표시 (쉼표로 구분된 목록):

`systemd-delta --type {{masked|equivalent|redirected|overridden|extended|unchanged}}`

- 지정된 접두사로 시작하는 경로의 파일만 표시 (참고: 접두사는 systemd 설정 파일이 있는 하위 디렉토리를 포함하는 디렉토리입니다):

`systemd-delta {{/etc|/run|/usr/lib|...}}`

- 접미사를 추가하여 검색 경로를 더 제한 (접두사는 선택 사항):

`systemd-delta {{접두사}}/{{tmpfiles.d|sysctl.d|systemd/system|...}}`
