# vainfo

> VA API 드라이버 정보 표시.
> 더 많은 정보: <https://wiki.archlinux.org/title/Hardware_video_acceleration#Verifying_VA-API>.

- 버전과 지원되는 entrypoint 표시:

`vainfo`

- 지정한 디스플레이 protocol 테스트:

`vainfo --display {{wayland|x11|drm|...}}`

- 사용 가능한 디스플레이 protocol 표시:

`vainfo --display help`

- 지원되는 entrypoint 표시:

`vainfo {{[-a|--all]}}`

- 도움말 표시:

`vainfo --help`
