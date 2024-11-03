# ipconfig

> Windows의 네트워크 구성을 표시하고 관리합니다.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- 모든 네트워크 어댑터 표시:

`ipconfig`

- 네트워크 어댑터의 자세한 목록을 표시:

`ipconfig /all`

- 네트워크 어댑터의 IP 주소 갱신:

`ipconfig /renew {{어댑터}}`

- 네트워크 어댑터의 IP 주소 해제:

`ipconfig /release {{어댑터}}`

- 로컬 DNS 캐시 표시:

`ipconfig /displaydns`

- 로컬 DNS 캐시의 모든 데이터 제거:

`ipconfig /flushdns`
