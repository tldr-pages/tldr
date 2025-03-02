# plasmashell

> Plasma 데스크톱을 시작하고 재시작합니다.
> 더 많은 정보: <https://invent.kde.org/plasma/plasma-desktop>.

- `plasmashell` 재시작:

`systemctl restart --user plasma-plasmashell`

- systemd 없이 `plasmashell` 재시작:

`plasmashell --replace & disown`

- 명령줄 옵션에 대한 도움말 표시:

`plasmashell {{[-h|--help]}}`

- Qt 옵션을 포함한 도움말 표시:

`plasmashell --help-all`
