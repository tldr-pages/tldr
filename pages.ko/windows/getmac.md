# getmac

> 시스템의 MAC 주소를 표시.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- 현재 시스템의 MAC 주소 표시:

`getmac`

- 특정 형식으로 세부 정보 표시:

`getmac /fo {{table|list|csv}}`

- 출력 목록에서 헤더 제외:

`getmac /nh`

- 원격 컴퓨터의 MAC 주소 표시:

`getmac /s {{호스트명}} /u {{사용자명}} /p {{비밀번호}}`

- 자세한 정보와 함께 MAC 주소 표시:

`getmac /v`

- 도움말 표시:

`getmac /?`
