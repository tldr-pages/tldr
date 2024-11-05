# pio access

> 레지스트리에 게시된 리소스(패키지)의 접근 수준 설정.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- 사용자에게 리소스 접근 권한 부여:

`pio access grant {{게스트|유지관리자|관리자}} {{사용자명}} {{리소스_URN}}`

- 사용자의 리소스 접근 권한 제거:

`pio access revoke {{사용자명}} {{리소스_URN}}`

- 사용자 또는 팀이 접근할 수 있는 모든 리소스와 접근 수준 표시:

`pio access list {{사용자명}}`

- 특정 사용자나 팀원에게만 리소스 접근 제한:

`pio access private {{리소스_URN}}`

- 모든 사용자에게 리소스 접근 허용:

`pio access public {{리소스_URN}}`
