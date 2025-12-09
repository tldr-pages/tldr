# cewl

> 웹 콘텐츠에서 크래킹용 단어 목록을 만드는 URL 수집 도구.
> 더 많은 정보: <https://digi.ninja/projects/cewl.php#usage>.

- 지정된 URL에서 링크 깊이 2까지 단어 목록 파일 생성:

`cewl {{[-d|--depth]}} 2 {{[-w|--write]}} {{경로/대상/단어목록.txt}} {{url}}`

- 지정된 URL에서 최소 5자 이상의 알파벳과 숫자로 이루어진 단어 목록 출력:

`cewl --with-numbers {{[-m|--min_word_length]}} 5 {{url}}`

- 디버그 모드로 이메일 주소를 포함한 지정된 URL에서 단어 목록 출력:

`cewl --debug {{[-e|--email]}} {{url}}`

- HTTP 기본 또는 다이제스트 인증을 사용하여 지정된 URL에서 단어 목록 출력:

`cewl --auth_type {{basic|digest}} --auth_user {{사용자명}} --auth_pass {{비밀번호}} {{url}}`

- 프록시를 통해 지정된 URL에서 단어 목록 출력:

`cewl --proxy_host {{호스트}} --proxy_port {{포트}} {{url}}`
