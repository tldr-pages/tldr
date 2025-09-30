# goldeneye.py

> HTTP DoS 테스트 도구.
> 더 많은 정보: <https://github.com/jseidl/GoldenEye>.

- 특정 웹사이트를 테스트:

`./goldeneye.py {{url}}`

- 100개의 사용자 에이전트와 200개의 동시 소켓으로 특정 웹사이트를 테스트:

`./goldeneye.py {{url}} --useragents 100 --sockets 200`

- SSL 인증서를 확인하지 않고 특정 웹사이트를 테스트:

`./goldeneye.py {{url}} --nosslcheck`

- 디버그 모드로 특정 웹사이트를 테스트:

`./goldeneye.py {{url}} --debug`

- 도움말 표시:

`./goldeneye.py --help`
