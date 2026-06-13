# systemctl hybrid-sleep

> suspend-to-RAM과 최대 절전을 결합한 하이브리드 절전 모드로 전환.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#hybrid-sleep>.

- 즉시 하이브리드 절전 모드로 전환:

`systemctl hybrid-sleep`

- inhibitor가 있어도 강제로 하이브리드 절전 모드로 전환:

`systemctl hybrid-sleep {{[-f|--force]}}`

- 로그인 사용자에게 알림 없이 하이브리드 절전 모드로 전환:

`systemctl hybrid-sleep --no-wall`
