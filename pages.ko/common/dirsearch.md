# dirsearch

> 웹 경로 스캐너.
> 더 많은 정보: <https://github.com/maurosoria/dirsearch>.

- 공통 확장자를 가진 공통 경로를 웹 서버에서 검색:

`dirsearch --url {{url}} --extensions-list`

- `.php` 확장자를 사용하여 일반 경로에 대한 웹 서버 목록을 스캔:

`dirsearch --url-list {{경로/대상/url-list.txt}} --extensions {{php}}`

- 공통 확장자를 사용하여 사용자 정의 경로를 웹 서버에서 검색:

`dirsearch --url {{url}} --extensions-list --wordlist {{경로/대상/url-paths.txt}}`

- 쿠키를 사용하여 웹 서버를 검색:

`dirsearch --url {{url}} --extensions {{php}} --cookie {{쿠키}}`

- `HEAD` HTTP 메소드를 사용하여 웹 서버를 스캔:

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- 웹 서버를 스캔하고, 결과를 `.json` 파일에 저장:

`dirsearch --url {{url}} --extensions {{php}} --json-report {{경로/대상/리포트.json}}`
