# systemctl preset-all

> 프리셋 정책 파일에 정의된 기본값에 따라, 설치된 모든 유닛의 활성화 상태를 재설정.
> 관련 항목: `systemctl preset`, `systemctl list-unit-files`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#preset-all>.

- 모든 설치된 유닛의 활성화 상태를 기본값으로 재설정:

`sudo systemctl preset-all`

- 프리셋 정책에서 활성화로 표시된 경우에만 활성화:

`sudo systemctl preset-all --preset-mode enable-only`

- 프리셋 정책에서 비활성화로 표시된 경우에만 비활성화:

`sudo systemctl preset-all --preset-mode disable-only`

- 출력 없이 종료 코드로만 처리:

`sudo systemctl preset-all {{[-q|--quiet]}}`
