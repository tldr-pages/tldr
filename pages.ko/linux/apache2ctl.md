# apache2ctl

> Apache HTTP 웹 서버 관리.
> 이 명령은 Debian 기반 OS에 포함되어 있으며, RHEL 기반 OS에서는 `httpd`를 참조하세요.
> 더 많은 정보: <https://manned.org/apache2ctl.8>.

- Apache 데몬 시작. 이미 실행 중인 경우 메시지 표시:

`sudo apache2ctl start`

- Apache 데몬 중지:

`sudo apache2ctl stop`

- Apache 데몬 재시작:

`sudo apache2ctl restart`

- 구성 파일의 구문 테스트:

`sudo apache2ctl -t`

- 로드된 모듈 나열:

`sudo apache2ctl -M`
