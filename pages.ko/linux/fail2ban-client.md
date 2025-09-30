# fail2ban-client

> fail2ban 서버를 구성하고 제어.
> 더 많은 정보: <https://manned.org/fail2ban-client>.

- 감옥 서비스의 현재 상태 검색:

`fail2ban-client status {{감옥}}`

- 지정된 IP를 감옥 서비스의 차단 목록에서 제거:

`fail2ban-client set {{감옥}} unbanip {{IP}}`

- fail2ban 서버가 실행 중인지 확인:

`fail2ban-client ping`
