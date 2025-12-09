# tspin

> `less` 페이지를 기반으로 하는 로그 파일 하이라이터로, 기본적으로 다른 페이지처럼 동작합니다.
> 더 많은 정보: <https://github.com/bensadeh/tailspin#settings>.

- 파일에서 읽고 `less`로 보기:

`tspin {{경로/대상/애플리케이션.log}}`

- 다른 명령어의 출력을 읽고 표준 출력으로 출력:

`journalctl -b --follow | tspin`

- 파일에서 읽고 `stdout`으로 출력:

`tspin {{경로/대상/애플리케이션.log}} --print`

- `stdin`에서 읽고 `stdout`으로 출력:

`echo "2021-01-01 12:00:00 [INFO] This is a log message" | tspin`
