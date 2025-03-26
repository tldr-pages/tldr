# semanage boolean

> SELinux 부울 설정을 영구적으로 관리합니다.
> 같이 보기: SELinux 정책 관리를 위한 `semanage`, 부울 값을 확인하기 위한 `getsebool`, 비영구적 부울 설정 적용을 위한 `setsebool`.
> 더 많은 정보: <https://manned.org/semanage-boolean>.

- 모든 부울 설정 나열:

`sudo semanage boolean {{[-l|--list]}}`

- 사용자 정의 부울 설정을 제목 없이 나열:

`sudo semanage boolean {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- 부울을 영구적으로 설정 또는 해제:

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
