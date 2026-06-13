# systemctl switch-root

> 새로운 루트 파일 시스템으로 전환하고 새로운 시스템 매니저를 실행.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#switch-root%20ROOT%20INIT>.

- 새로운 루트 파일 시스템으로 전환하고 기본 init 시스템 실행:

`systemctl switch-root {{경로/대상/새로운_루트}}`

- 새로운 루트 파일 시스템으로 전환하고 특정 init 바이너리 실행:

`systemctl switch-root {{경로/대상/새로운_루트}} {{/sbin/init}}`

- 자세한 출력과 함께 새로운 루트 파일 시스템으로 전환:

`systemctl switch-root {{경로/대상/새로운_루트}} {{[-v|--verbose]}}`
