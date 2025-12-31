# setsebool

> SELinux 불리언 값을 설정합니다.
> 같이 보기: `semanage-boolean`, `getsebool`.
> 더 많은 정보: <https://manned.org/setsebool>.

- 모든 불리언의 현재 설정을 표시:

`getsebool -a`

- 불리언을 일시적으로 설정 또는 해제 (재부팅 시 비활성화):

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- 불리언을 영구적으로 설정 또는 해제:

`sudo setsebool -P {{container_use_devices}} {{1|true|on|0|false|off}}`

- 여러 불리언을 한 번에 영구적으로 설정 또는 해제:

`sudo setsebool -P {{ftpd_use_fusefs=1 mount_anyfile=0 ...}}`

- 불리언을 영구적으로 설정 또는 해제 (대안 방법으로 `semanage-boolean` 사용):

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
