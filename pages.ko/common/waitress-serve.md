# waitress-serve

> 순수 Python WSGI HTTP 서버.
> 더 많은 정보: <https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html>.

- Python 웹 앱 실행:

`waitress-serve {{임포트.경로:wsgi_함수}}`

- localhost의 포트 8080에서 수신 대기:

`waitress-serve --listen={{localhost}}:{{8080}} {{임포트.경로:wsgi_함수}}`

- Unix 소켓에서 waitress 시작:

`waitress-serve --unix-socket={{경로/대상/소켓}} {{임포트.경로:wsgi_함수}}`

- 4개의 스레드를 사용하여 요청 처리:

`waitress-serve --threads={{4}} {{임포트.경로:wsgi_함수}}`

- WSGI 객체를 반환하는 팩토리 메서드 호출:

`waitress-serve --call {{임포트.경로.wsgi_팩토리}}`

- HTTPS URL 스킴 사용:

`waitress-serve --url-scheme={{https}} {{임포트.경로:wsgi_함수}}`
