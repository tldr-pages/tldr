# gunicorn

> Python WSGI HTTP 서버.
> 더 많은 정보: <https://docs.gunicorn.org/en/latest/run.html>.

- Python 웹 애플리케이션 실행:

`gunicorn {{import.path:app_object}}`

- localhost의 포트 8080에서 수신 대기:

`gunicorn --bind {{localhost}}:{{8080}} {{import.path:app_object}}`

- 실시간 새로고침을 켜기:

`gunicorn --reload {{import.path:app_object}}`

- 요청 처리를 위해 4개의 작업자 프로세스를 사용:

`gunicorn --workers {{4}} {{import.path:app_object}}`

- 요청 처리를 위해 4개의 작업자 스레드를 사용:

`gunicorn --threads {{4}} {{import.path:app_object}}`

- Run app over HTTPS를 통해 애플리케이션을 실행:

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{import.path:app_object}}`
