# systemctl revert

> 유닛 파일을 벤더 기본 버전으로 되돌림.
> `edit`, `enable`, `disable`, `set-property`, `mask` 등의 변경 사항을 되돌림.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#revert%20UNIT%E2%80%A6>.

- 유닛 파일을 기본 설정으로 복원:

`systemctl revert {{유닛1 유닛2 ...}}`

- 사용자 유닛 파일 복원:

`systemctl revert {{유닛}} --user`
