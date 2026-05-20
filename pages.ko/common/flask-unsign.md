# flask-unsign

> `Flask` 세션 쿠키를 브루트포스, 디코딩 및 생성하는 도구.
> 더 많은 정보: <https://github.com/Paradoxis/Flask-Unsign>.

- Flask 세션 쿠키 디코딩:

`flask-unsign {{[-d|--decode]}} {{[-c|--cookie]}} {{쿠키}}`

- `Set-Cookie` 헤더를 반환하는 URL에서 세션 쿠키를 가져와 디코딩:

`flask-unsign {{[-d|--decode]}} --server {{URL}}`

- 기본 flask-unsign-wordlist를 사용하여 시크릿 키 브루트포스 수행 (`flask-unsign-wordlist` 필요):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{쿠키}}`

- 사용자 지정 wordlist를 사용하여 시크릿 키 브루트포스 수행 (`--no-literal-eval`은 따옴표 없는 항목 처리 시 사용):

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{경로/대상/wordlist.txt}}`

- 시크릿 키를 사용하여 새로운 세션 쿠키 서명 생성:

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} "{{{'logged_in': False}}}" {{[-S|--secret]}} {{시크릿}}`

- 레거시 타임스탬프를 사용하여 세션 쿠키 서명 생성 (오래된 버전 호환 목적):

`flask-unsign {{[-s|--sign]}} {{[-c|--cookie]}} "{{{'logged_in': False}}}" {{[-S|--secret]}} {{시크릿}} {{[-l|--legacy]}}`

- 사용자 지정 스레드 수와 literal evaluation 비활성화 옵션으로 세션 쿠키 브루트포스 수행:

`flask-unsign {{[-u|--unsign]}} {{[-c|--cookie]}} {{cookie}} {{[-w|--wordlist]}} {{경로/대상/wordlist.txt}} {{[-t|--threads]}} {{스레드}} {{[-nE|--no-literal-eval]}}`
