# arjun

> 웹 애플리케이션의 HTTP 파라미터를 탐지.
> 더 많은 정보: <https://github.com/s0md3v/Arjun/wiki/Usage>.

- URL에서 GET 파라미터를 스캔:

`arjun -u {{https://example.com/page.php}}`

- POST 메서드를 사용하여 스캔:

`arjun -u {{https://example.com/api}} -m POST`

- 탐지된 파라미터를 JSON 파일로 저장:

`arjun -u {{https://example.com}} -o {{경로/대상/출력파일.json}}`

- 사용자 정의 워드리스트를 사용:

`arjun -u {{https://example.com}} -w {{path/to/wordlist.txt}}`

- 요청 사이의 지연 시간을 늘려 rate limiting을 방지:

`arjun -u {{https://example.com}} -d {{2}}`
