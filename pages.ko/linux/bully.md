# bully

> 무선 액세스 포인트의 WPS 핀을 무차별 대입으로 알아냅니다.
> `bully`를 사용하기 전에 필요한 정보를 `airmon-ng` 및 `airodump-ng`로 수집해야 합니다.
> 더 많은 정보: <https://salsa.debian.org/pkg-security-team/bully>.

- 비밀번호 크랙:

`bully --bssid "{{맥}}" --channel "{{채널}}" --bruteforce "{{인터페이스}}"`

- 도움말 표시:

`bully --help`
