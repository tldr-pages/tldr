# systemctl edit

> systemd 유닛 파일을 편집.
> 관련 항목: `systemctl revert`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#edit%20UNIT%E2%80%A6>.

- 기존 유닛 파일을 변경하지 않고 오버레이로 수정:

`sudo systemctl edit {{유닛_파일}}`

- 유닛 파일을 직접 편집:

`sudo systemctl edit {{유닛_파일}} {{[-l|--full]}}`

- 새로운 유닛 파일 생성:

`sudo systemctl edit {{유닛_파일}} {{[-lf|--full --force]}}`

- 사용자 유닛 파일을 오버레이로 수정:

`systemctl edit {{유닛_파일}} --user`
