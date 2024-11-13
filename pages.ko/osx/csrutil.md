# csrutil

> 시스템 무결성 보호 설정 관리.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/csrutil.8.html>.

- 시스템 무결성 보호 상태 표시:

`csrutil status`

- 시스템 무결성 보호 비활성화:

`csrutil disable`

- 시스템 무결성 보호 활성화:

`csrutil enable`

- 허용된 NetBoot 소스 목록 표시:

`csrutil netboot list`

- 허용된 NetBoot 소스 목록에 IPv4 주소 추가:

`csrutil netboot add {{ip}}`

- 시스템 무결성 보호 상태 초기화 및 NetBoot 목록 초기화:

`csrutil clear`
