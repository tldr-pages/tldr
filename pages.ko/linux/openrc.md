# openrc

> OpenRC 서비스 관리자.
> 같이 보기: `rc-status`, `rc-update`, `rc-service`.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/OpenRC>.

- 특정 런레벨로 변경:

`sudo openrc {{런레벨_이름}}`

- 기존 서비스를 중지하지 않고 특정 런레벨로 변경:

`sudo openrc --no-stop {{런레벨_이름}}`
