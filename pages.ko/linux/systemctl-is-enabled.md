# systemctl is-enabled

> 유닛 파일이 활성화되어 있는지 확인.
> 관련 항목: `systemctl enable`, `systemctl disable`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-enabled%20UNIT%E2%80%A6>.

- 활성화 상태 출력:

`systemctl is-enabled {{유닛1 유닛2 ...}}`

- 출력 없이 종료 코드로만 확인:

`systemctl is-enabled {{유닛}} {{[-q|--quiet]}}`

- 설치된 타겟과 심볼릭 링크 경로까지 상세 출력:

`systemctl is-enabled {{유닛}} {{[-l|--full]}}`
