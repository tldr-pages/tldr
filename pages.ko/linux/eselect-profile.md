# eselect profile

> 시스템 프로필을 설정하는 `/etc/portage/make.profile` 심볼릭 링크를 관리하는 `eselect` 모듈.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- 사용 가능한 프로필 심볼릭 링크 대상과 그 번호 나열:

`eselect profile list`

- `list` 명령어의 이름 또는 번호로 `/etc/portage/make.profile` 심볼릭 링크 설정:

`eselect profile set {{이름|번호}}`

- 현재 시스템 프로필 표시:

`eselect profile show`
