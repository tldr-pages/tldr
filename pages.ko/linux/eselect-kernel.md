# eselect kernel

> `/usr/src/linux` 심볼릭 링크를 관리하기 위한 `eselect` 모듈.
> 더 많은 정보: <https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- 사용 가능한 커널 심볼릭 링크 대상과 해당 번호 나열:

`eselect kernel list`

- `list` 명령어의 이름이나 번호로 `/usr/src/linux` 심볼릭 링크 설정:

`eselect kernel set {{이름|번호}}`

- 현재 커널 심볼릭 링크가 가리키는 대상을 표시:

`eselect kernel show`

- 현재 실행 중인 커널로 커널 심볼릭 링크 설정:

`eselect kernel update`
