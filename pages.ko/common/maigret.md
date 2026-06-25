# maigret

> 수천 개 웹사이트에서 사용자명을 기반으로 OSINT 정보 수집.
> 참고: The Maigret 데이터베이스는 도구에 포함된 로컬 JSON 파일을 사용.
> 관련 항목: `sherlock`.
> 더 많은 정보: <https://maigret.readthedocs.io/en/latest/usage-examples.html>.

- Maigret 데이터베이스를 사용하여 하나 이상의 사용자명 검색:

`maigret {{사용자명1 사용자명2 ...}}`

- 계정 검색 후 다양한 형식의 보고서 생성:

`maigret {{사용자명}} {{--txt|--csv|--html|--xmind|--pdf|--graph|--json simple|--json ndjson}}`

- 프록시를 통해 검색 요청 전송:

`maigret {{사용자명}} {{[-p|--proxy]}} {{socks5://127.0.0.1:9050|http://127.0.0.1:8080}}`

- Maigret Web Interface 실행 (기본 포트는 `5000`):

`maigret --web {{5000}}`

- Maigret 데이터베이스의 상위 N개 사이트만 대상으로 검색:

`maigret {{사용자명}} --top-sites {{500}}`

- Maigret 데이터베이스에 등록된 모든 사이트 검색:

`maigret {{사용자명}} {{[-a|--all-sites]}}`

- 특정 사이트 대상으로만 검색 (목표가 있거나, 빠른 검색에서 유용):

`maigret {{사용자명}} --site {{twitter}} --site {{github}}`
