# clamscan

> 바이러스 검사를 하는 줄 명령어.
> 더 많은 정보: <https://www.clamav.net>.

- 약점이 있는 파일을 검사합니다:

`clamscan {{path/to/file}}`

- 특정 디렉토리의 모든 파일을 재귀적으로 검사합니다:

`clamscan -r {{path/to/directory}}`

- `stdin` 으로부터 데이터를 검사합니다:

`{{command}} | clamscan -`

- 바이러스 데이터베이스 파일 또는 파일 디렉토리 지정합니다:

`clamscan --database {{path/to/database_file_or_directory}}`

- 현재 디렉토리를 검색하고 감염된 파일만 출력합니다:

`clamscan --infected`

- 검사한 리포트를 로그 파일로 내보냅니다:

`clamscan --log {{path/to/log_file}}`

- 특정 디렉토리로 감염된 파일을 보냅니다:

`clamscan --move {{path/to/quarantine_directory}}`

- 감연된 파일을 제거합니다:

`clamscan --remove yes`
