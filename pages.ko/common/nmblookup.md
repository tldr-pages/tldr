# nmblookup

> SMB 공유를 검색.
> 더 많은 정보: <https://www.samba.org/samba/docs/current/man-html/nmblookup.1.html>.

- 로컬 네트워크에서 SMB 공유가 있는 호스트 찾기:

`nmblookup -S '*'`

- SAMBA에 의해 실행되는 SMB 공유가 있는 로컬 네트워크의 호스트 찾기:

`nmblookup --status __SAMBA__`
