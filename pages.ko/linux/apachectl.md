# apachectl

> Apache HTTP 서버를 제어하는 도구.
> 더 많은 정보: <https://manned.org/apachectl>.

- 서버 시작:

`sudo apachectl start`

- 서버 재시작:

`sudo apachectl restart`

- 서버 중지:

`sudo apachectl stop`

- 설정 파일 유효성 검사:

`apachectl configtest`

- 서버 상태 확인 (lynx 브라우저 필요):

`apachectl status`

- 연결을 끊지 않고 설정 재로드:

`sudo apachectl graceful`

- 전체 Apache 설정 출력 (항상 지원되지는 않음):

`apachectl -S`

- 도움말 표시:

`apachectl -h`
