# driverquery

> 설치된 장치 드라이버에 대한 정보를 표시.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- 설치된 모든 장치 드라이버 목록 표시:

`driverquery`

- 지정된 형식으로 드라이버 목록 표시:

`driverquery /fo {{table|list|csv}}`

- 서명 여부를 나타내는 열과 함께 드라이버 목록 표시:

`driverquery /si`

- 출력 목록에서 헤더 제외:

`driverquery /nh`

- 원격 컴퓨터의 드라이버 목록 표시:

`driverquery /s {{호스트명}} /u {{사용자명}} /p {{비밀번호}}`

- 자세한 정보와 함께 드라이버 목록 표시:

`driverquery /v`

- 도움말 표시:

`driverquery /?`
