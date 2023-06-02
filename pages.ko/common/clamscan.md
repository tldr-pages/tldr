# clamscan

> 바이러스 검사를 하는 줄 명령어.
> 더 많은 정보: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- 약점이 있는 파일을 검사합니다:

`clamscan {{경로/파일}}`

- 특정 디렉토리의 모든 파일을 재귀적으로 검사합니다:

`clamscan -r {{경로/디렉토리}}`

- stdin 으로부터 데이터를 검사합니다:

`{{명령어}} | clamscan -`

- 바이러스 데이터베이스 파일 또는 파일 디렉토리 지정합니다:

`clamscan --database {{경로/데이터베이스_파일_혹은_디렉토리}}`

- 현재 디렉토리를 검색하고 감염된 파일만 출력합니다:

`clamscan --infected`

- 검사한 리포트를 로그 파일로 내보냅니다:

`clamscan --log {{경로/로그파일}}`

- 특정 디렉토리로 감염된 파일을 보냅니다:

`clamscan --move {{경로/감염된_디렉토리}}`

- 감연된 파일을 제거합니다:

`clamscan --remove yes`
