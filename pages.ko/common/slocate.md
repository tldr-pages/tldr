# slocate

> GNU Locate의 보안 강화 버전.
> 관련 항목: `locate`.
> 더 많은 정보: <https://manned.org/slocate>.

- 에러 메시지를 숨기기 위해 조용한 모드를 활성화:

`slocate -q`

- 표시할 결과 수를 제한:

`slocate -n {{번호}}`

- `/` 경로부터 시작하여 `slocate` 데이터베이스를 생성:

`slocate -u`

- 지정한 디렉터리에서 시작하여 `slocate` 데이터베이스를 생성:

`slocate -U {{경로/대상/디렉터리}}`

- 기본 `/etc/updatedb.conf` 설정을 사용해 `slocate` 데이터베이스를 업데이트:

`slocate -c`

- `slocate`의 보안 수준을 설정, `0`은 비활성화, `1`은 보안 모드:

`slocate -l {{0|1}}`

- 검색할 `slocate` 데이터베이스를 지정:

`slocate {{[-d|--database]}} {{경로/대상/디렉터리}}`

- 지정한 `regex` 문자열을 사용하여 `slocate` 데이터베이스를 검색:

`slocate {{[-r|--regexp]}} {{regex}}`
