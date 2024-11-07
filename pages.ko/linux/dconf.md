# dconf

> dconf 데이터베이스 관리.
> 같이 보기: `dconf-read`, `dconf-reset`, `dconf-write`, `gsettings`.
> 더 많은 정보: <https://manned.org/dconf>.

- 특정 키 값을 출력:

`dconf read {{/경로/대상/키}}`

- 특정 경로의 하위 디렉토리 및 하위 키를 출력:

`dconf list {{/경로/대상/폴더/}}`

- 특정 키 값 쓰기:

`dconf write {{/경로/대상/키}} "{{값}}"`

- 특정 키 값 초기화:

`dconf reset {{/경로/대상/키}}`

- 특정 키/디렉토리의 변경 사항 감시:

`dconf watch {{/경로/대상/키|/경로/대상/폴더/}}`

- 특정 디렉토리를 INI 파일 형식으로 덤프:

`dconf dump {{/경로/대상/폴더/}}`
