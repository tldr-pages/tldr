# crond

> crontab 파일에 등록된 예약 명령을 실행하는 데몬.
> 더 많은 정보: <https://manned.org/crond>.

- 백그라운드에서 데몬을 시작하고 예약된 명령 확인:

`crond`

- 포그라운드에서 데몬을 시작하고 예약된 명령 확인:

`crond -n`

- 데몬의 작업 출력을 시스템([s]ystem) 로그로 전송:

`crond -s`

- 기본 제한을 무시하고 사용자 지정 crontab 파일 허용:

`crond -p`

- 환경 설정에서 crontab 파일 경로 상속:

`crond -P`
