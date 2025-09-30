# aa-status

> 현재 로드된 AppArmor 모듈 나열.
> 같이 보기: `aa-complain`, `aa-disable`, `aa-enforce`.
> 더 많은 정보: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- 상태 확인:

`sudo aa-status`

- 로드된 정책의 수 표시:

`sudo aa-status --profiled`

- 로드된 시행 정책의 수 표시:

`sudo aa-status --enforced`

- 로드된 비시행 정책의 수 표시:

`sudo aa-status --complaining`

- 작업을 종료하는 로드된 시행 정책의 수 표시:

`sudo aa-status --kill`
