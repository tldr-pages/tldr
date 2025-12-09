# kate

> KDE의 고급 텍스트 편집기.
> 더 많은 정보: <https://docs.kde.org/stable/en/kate/kate/fundamentals.html#starting-from-the-command-line>.

- 특정 파일 열기:

`kate {{경로/대상/파일1 경로/대상/파일2 ...}}`

- 특정 원격 파일 열기:

`kate {{https://example.com/경로/대상/파일1 https://example.com/경로/대상/파일2 ...}}`

- 이미 열려 있는 경우에도 새 편집기 인스턴스 생성:

`kate --new`

- 특정 줄에 커서를 놓고 파일 열기:

`kate --line {{줄_번호}} {{경로/대상/파일}}`

- 특정 줄과 열에 커서를 놓고 파일 열기:

`kate --line {{줄_번호}} --column {{열_번호}} {{경로/대상/파일}}`

- `stdin`에서 파일 생성:

`cat {{경로/대상/파일}} | kate --stdin`

- 도움말 표시:

`kate --help`
