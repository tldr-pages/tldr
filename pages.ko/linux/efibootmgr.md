# efibootmgr

> UEFI 부트 매니저를 조작합니다.
> 더 많은 정보: <https://manned.org/efibootmgr>.

- 부트 옵션과 해당 번호를 모두 나열:

`efibootmgr {{-u|--unicode}}`

- UEFI Shell v2를 부트 옵션으로 추가:

`sudo efibootmgr -c -d {{/dev/sda}} -p {{1}} -l "{{\경로\대상\shell.efi}}" -L "{{UEFI Shell}}"`

- Linux를 부트 옵션으로 추가:

`sudo efibootmgr --create --disk {{/dev/sda}} --part {{1}} --loader "{{\vmlinuz}}" --unicode "{{kernel_cmdline}}" --label "{{Linux}}"`

- 현재 부트 순서 변경:

`sudo efibootmgr {{-o|--bootorder}} {{0002,0008,0001,0005}}`

- 부트 옵션 삭제:

`sudo efibootmgr {{-b|--bootnum}} {{0008}} {{-B|--delete-bootnum}}`
