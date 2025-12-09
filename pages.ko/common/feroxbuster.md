# feroxbuster

> Rust로 작성된 간단하고 빠르며 반복적인 콘텐츠 검색 도구.
> 웹 서버 등에서 숨겨진 경로를 무차별 공격하는 데 사용됨.
> 더 많은 정보: <https://epi052.github.io/feroxbuster-docs/docs/>.

- 확장자, 100개의 스레드 및 임의의 사용자 에이전트가 포함된 단어 목록에서 일치하는 특정 디렉터리 및 파일 검색:

`feroxbuster --url "{{https://example.com}}" --wordlist {{경로/대상/파일}} --threads {{100}} --extensions "{{php,txt}}" --random-agent`

- 특정 프록시를 통해 재귀 없이 디렉터리를 열거:

`feroxbuster --url "{{https://example.com}}" --wordlist {{경로/대상/파일}} --no-recursion --proxy "{{http://127.0.0.1:8080}}"`

- 웹페이지에서 링크 찾기:

`feroxbuster --url "{{https://example.com}}" --extract-links`

- 특정 상태 코드 및 문자 수로 필터링:

`feroxbuster --url "{{https://example.com}}" --filter-status {{301}} --filter-size {{4092}}`
