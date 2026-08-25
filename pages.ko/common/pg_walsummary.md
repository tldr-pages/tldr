# pg_walsummary

> WAL 요약 파일의 내용을 출력.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgwalsummary.html>.

- WAL 요약 파일을 텍스트로 변환하여 출력:

`pg_walsummary {{경로/대상/파일}}`

- 수정된 각 블록을 개별 항목으로 출력 (범위 출력이 아님):

`pg_walsummary {{[-i|--individual]}} {{경로/대상/파일}}`

- 일반 출력은 생략하고 오류만 표시:

`pg_walsummary {{[-q|--quiet]}} {{경로/대상/파일}}`
