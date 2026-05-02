# nagios

> 호스트/서비스/네트워크 모니터링을 위한 레거시 프로그램.
> 현재는 `nagios4`로 대부분 대체됨.
> 관련 항목: `nagios2`, `nagios3`, `nagios4`.
> 더 많은 정보: <https://manned.org/nagios>.

- `nagios` 시작:

`nagios /etc/nagios/nagios.cfg`

- 데몬 모드로 `nagios` 실행:

`nagios -d`

- `nagios` 시작 후, 서비스 체크 스케줄링 정보를 `stdout`에 출력한 뒤, 종료:

`nagios -s`

- 설정 파일 검증:

`nagios -v`
