# supervisord

> Supervisor는 유닉스 계열 운영 체제에서 일부 프로세스를 제어하기 위한 클라이언트/서버 시스템입니다.
> Supervisord는 Supervisor의 서버 부분으로, 주로 구성 파일을 통해 관리됩니다.
> 더 많은 정보: <https://supervisord.org/running.html#running-supervisord>.

- 지정된 구성 파일로 `supervisord` 시작:

`supervisord -c {{경로/대상/파일}}`

- 포그라운드에서 supervisord 실행:

`supervisord -n`
