# systemctl bind

> 호스트의 파일 또는 디렉터리를 유닛의 마운트 네임스페이스에 일시적으로 bind-mount를 함.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#bind%20UNIT%20PATH%20%5BPATH%5D>.

- 호스트 경로를 유닛 내부의 동일한 위치에 Bind-mount:

`systemctl bind {{유닛}} /{{경로/대상/호스트_디렉토리}}`

- 호스트 경로를 유닛 내부의 다른 위치에 Bind-mount:

`systemctl bind {{유닛}} /{{경로/대상/호스트_디렉토리}} /{{경로/대상/유닛_디렉토리}}`

- 유닛 내부에서 읽기 전용으로 Bind-mount:

`systemctl bind {{유닛}} /{{경로/대상/호스트_디렉토리}} --read-only`

- binding 전에 유닛 내부에 대상 경로 생성:

`systemctl bind {{유닛}} /{{경로/대상/호스트_디렉토리}} /{{경로/대상/유닛_디렉토리}} --mkdir`
