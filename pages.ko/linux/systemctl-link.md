# systemctl link

> 유닛 파일 검색 경로 밖에 있는 유닛 파일을 검새 경로에 연결.
> 관련 항목: `systemctl disable`.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#link%20PATH%E2%80%A6>.

- systemd 명령에서 사용할 수 있도록 유닛 파일 연결:

`systemctl link {{경로/대상/서비스}}`

- 여러 유닛 파일을 한 번에 연결:

`systemctl link {{경로/대상/서비스1 경로/대상/서비스2 ...}}`
