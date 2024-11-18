# pvscan

> 모든 물리적 볼륨을 나열하고 온라인 상태를 관리합니다.
> 더 많은 정보: <https://manned.org/pvscan>.

- 모든 물리적 볼륨 나열:

`pvscan`

- 특정 물리적 볼륨을 사용하는 볼륨 그룹 표시:

`pvscan --cache --listvg {{/dev/sdX}}`

- 특정 물리적 볼륨을 사용하는 논리 볼륨 표시:

`pvscan --cache --listlvs {{/dev/sdX}}`

- JSON 형식으로 자세한 정보 표시:

`pvscan --reportformat json`
