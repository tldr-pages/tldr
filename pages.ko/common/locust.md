# locust

> 시스템이 처리할 수 있는 동시 사용자 수를 결정하는 부하 테스트 도구.
> 더 많은 정보: <https://docs.locust.io/en/stable/configuration.html#configuration>.

- locustfile.py를 사용하여 "example.com"에 웹 인터페이스로 부하 테스트:

`locust --host={{http://example.com}}`

- 다른 테스트 파일 사용:

`locust --locustfile={{테스트_파일.py}} --host={{http://example.com}}`

- 웹 인터페이스 없이 테스트 실행, 1초에 1명의 사용자를 추가하여 100명의 사용자가 될 때까지:

`locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}`

- Locust를 마스터 모드로 시작:

`locust --master --host={{http://example.com}}`

- Locust 슬레이브를 마스터에 연결:

`locust --slave --host={{http://example.com}}`

- 다른 기기에 있는 마스터에 Locust 슬레이브 연결:

`locust --slave --master-host={{마스터_호스트명}} --host={{http://example.com}}`
