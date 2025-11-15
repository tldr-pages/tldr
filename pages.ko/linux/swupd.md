# swupd

> Clear Linux의 패키지 관리 도구.
> 더 많은 정보: <https://www.clearlinux.org/clear-linux-documentation/guides/clear/swupd.html>.

- 최신 버전으로 업데이트:

`sudo swupd update`

- 현재 버전을 표시하고, 새 버전이 있는지 확인:

`swupd check-update`

- 설치된 번들 나열:

`swupd bundle-list`

- 원하는 패키지가 존재하는 번들 찾기:

`swupd search -b {{패키지}}`

- 새 번들 설치:

`sudo swupd bundle-add {{번들}}`

- 번들 제거:

`sudo swupd bundle-remove {{번들}}`

- 손상되었거나 누락된 파일 수정:

`sudo swupd verify`
