# systemctl preset

> 프리셋 정책 파일에 정의된 기본값에 따라, 유닛 파일의 활성화 상태를 재설정.
> 관련 항목: `systemctl preset-all`, `systemctl list-unit-files`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#preset%20UNIT%E2%80%A6>.

- 프리셋 기본값으로 활성화 상태 재설정:

`systemctl preset {{유닛1 유닛2 ...}}`

- 프리셋 정책에서 활성화로 표시된 경우에만 활성화:

`systemctl preset {{유닛}} --preset-mode enable-only`

- 프리셋 정책에서 비활성화로 표시된 경우에만 비활성화:

`systemctl preset {{유닛}} --preset-mode disable-only`

- 출력 없이 종료 코드로만 처리:

`systemctl preset {{유닛}} {{[-q|--quiet]}}`
