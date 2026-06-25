# aa-unconfined

> AppArmor 프로파일이 적용되지 않은 상태에서 TCP/UDP 포트를 열고 있는 프로세스를 나열.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-unconfined.8>.

- `ss` 명령(기본 동작)으로 unconfined 프로세스 목록 출력 :

`sudo aa-unconfined`

- `ss` 대신 `netstat`을 사용해 열린 소켓 감지:

`sudo aa-unconfined --with-netstat`

- `/proc`의 모든 프로세스를 대상으로 TCP/UDP 포트 및 AppArmor 프로파일 미적용 여부를 상세 출력:

`sudo aa-unconfined --paranoid`

- 도움말 표시:

`aa-unconfined {{[-h|--help]}}`
