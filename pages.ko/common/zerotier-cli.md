# zerotier-cli

> 로컬 ZeroTier 가상 네트워크 서비스를 제어.
> 관련 항목: `zerotier-idtool`, `zerotier-one`.
> 더 많은 정보: <https://github.com/zerotier/ZeroTierOne/blob/main/doc/zerotier-cli.1.md>.

- 네트워크에 참여:

`sudo zerotier-cli join {{네트워크_아이디}}`

- 네트워크 목록 표시:

`sudo zerotier-cli listnetworks`

- 피어 목록을 읽기 쉬운 형식으로 표시:

`sudo zerotier-cli peers`

- 네트워크에서 나가기:

`sudo zerotier-cli leave {{네트워크_아이디}}`

- ZeroTier One 상태 표시:

`sudo zerotier-cli {{[info|status]}}`
