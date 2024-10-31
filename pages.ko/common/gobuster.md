# gobuster

> 웹 서버 등의 숨겨진 경로를 무차별 공격.
> 더 많은 정보: <https://github.com/OJ/gobuster>.

- 단어 목록에서 일치하는 디렉터리와 파일을 검색:

`gobuster dir --url {{https://example.com/}} --wordlist {{경로/대상/파일}}`

- 하위 도메인 검색:

`gobuster dns --domain {{example.com}} --wordlist {{경로/대상/파일}}`

- Amazon S3 버킷 검색:

`gobuster s3 --wordlist {{경로/대상/파일}}`

- 서버에서 다른 가상 호스트를 검색:

`gobuster vhost --url {{https://example.com/}} --wordlist {{경로/대상/파일}}`

- 매개변수 값을 퍼징:

`gobuster fuzz --url {{https://example.com/?parameter=FUZZ}} --wordlist {{경로/대상/파일}}`

- 매개변수 이름을 퍼징:

`gobuster fuzz --url {{https://example.com/?FUZZ=value}} --wordlist {{경로/대상/파일}}`
