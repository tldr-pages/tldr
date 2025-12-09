# gpasswd

> `/etc/group` 및 `/etc/gshadow`를 관리합니다.
> 더 많은 정보: <https://manned.org/gpasswd>.

- 그룹 관리자 정의:

`sudo gpasswd {{[-A|--administrators]}} {{사용자1,사용자2}} {{그룹}}`

- 그룹 구성원 목록 설정:

`sudo gpasswd {{[-M|--members]}} {{사용자1,사용자2}} {{그룹}}`

- 지정된 그룹에 비밀번호 생성:

`gpasswd {{그룹}}`

- 지정된 그룹에 사용자 추가:

`gpasswd {{[-a|--add]}} {{사용자}} {{그룹}}`

- 지정된 그룹에서 사용자 제거:

`gpasswd {{[-d|--delete]}} {{사용자}} {{그룹}}`
