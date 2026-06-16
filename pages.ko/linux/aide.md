# aide

> 파일 무결성을 검증하기 위한 고급 침임 탐지 환경.
> 더 많은 정보: <https://manned.org/aide>.

- 데이터베이스 초기화:

`sudo aide {{[-i|--init]}}`

- 데이터베이스의 불일치 여부 검사:

`sudo aide {{[-C|--check]}}`

- 설정 파일 정의에 따라 두 데이터베이스를 비교:

`sudo aide {{[-E|--compare]}}`

- 비대화식으로 검사 후 데이터베이스 업데이트:

`sudo aide {{[-u|--update]}}`

- 기본 `aide.conf` 대신 사용할 설정 파일 지정:

`sudo aide {{[-c|--config]}} {{경로/대상/설정_파일}}`

- 특정 문자열에 대해 `regex`로 검사 AIDE 범위 제한:

`sudo aide {{[-l|--limit]}} {{regex}}`

- 리포트 결과를 URL로 전송:

`sudo aide {{[-r|--report]}} {{리포트_주소}}`
