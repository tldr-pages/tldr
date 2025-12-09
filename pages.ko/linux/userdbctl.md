# userdbctl

> 시스템의 사용자, 그룹 및 그룹 멤버십을 검사합니다.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/userdbctl.html>.

- 모든 알려진 사용자 기록 나열:

`userdbctl user`

- 특정 사용자 세부 정보 표시:

`userdbctl user {{사용자명}}`

- 모든 알려진 그룹 나열:

`userdbctl group`

- 특정 그룹 세부 정보 표시:

`userdbctl group {{그룹명}}`

- 현재 시스템에 사용자/그룹 정의를 제공하는 모든 서비스 나열:

`userdbctl services`
