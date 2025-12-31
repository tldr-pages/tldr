# dalfox

> 자동화에 중점을 둔 강력한 오픈소스 XSS 스캐너.
> 더 많은 정보: <https://dalfox.hahwul.com/page/usage/>.

- XSS 취약점에 대한 단일 URL을 스캔:

`dalfox url {{http://example.com}}`

- 인증을 위해 헤더를 사용해 URL을 스캔:

`dalfox url {{http://example.com}} -H {{'X-My-Header: 123'}}`

- 파일에서 URL 목록을 스캔:

`dalfox file {{경로/대상/파일}}`
