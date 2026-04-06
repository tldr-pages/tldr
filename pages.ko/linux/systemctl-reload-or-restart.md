# systemctl reload-or-restart

> `systemd` 유닛들을 재로드 할 수 있다면 다시 불러오고, 그렇지 않으면 다시 시작.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reload-or-restart%20PATTERN%E2%80%A6>.

- 유닛 재로드 또는 재시작:

`systemctl reload-or-restart {{유닛}}`

- 패턴과 일치하는 여러 유닛 재로드 또는 재시작:

`systemctl reload-or-restart {{패턴}}`

- 작업 완료를 기다리지 않고 실행:

`systemctl reload-or-restart {{유닛}} --no-block`

- 사용자 유닛에만 적용:

`systemctl reload-or-restart {{유닛}} --user`
