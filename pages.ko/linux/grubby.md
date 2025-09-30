# grubby

> `grub` 및 `zipl` 부트로더를 설정하는 도구.
> 더 많은 정보: <https://manned.org/grubby.8>.

- 모든 커널 메뉴 항목에 커널 부팅 인자 추가:

`sudo grubby --update-kernel=ALL --args '{{quiet console=ttyS0}}'`

- 기본 커널 항목에서 기존 인자 제거:

`sudo grubby --update-kernel=DEFAULT --remove-args {{quiet}}`

- 모든 커널 메뉴 항목 나열:

`sudo grubby --info=ALL`
