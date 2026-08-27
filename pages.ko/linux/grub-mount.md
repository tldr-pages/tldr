# grub-mount

> Mount a filesystem or filesystem image read-only using GRUB's filesystem drivers.
> 더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmount>.

- 블록 장치 또는 파일 시스템 이미지를 지정한 마운트 지점에 마운트:

`grub-mount {{/dev/sdXY}} {{/mnt}}`

- 디스크 이미지의 2번째 파티션을 마운트 (`-r`: 이미지 내 파티션 번호 지정):

`grub-mount {{[-r|--root]}} {{2}} {{disk.img}} {{/mnt}}`

- 암호화된 장치를 마운트하고 암호 입력을 요청:

`grub-mount {{[-C|--crypto]}} {{/dev/sdXY}} {{/mnt}}`

- 파일에서 ZFS 암호화 키를 로드하여 마운트:

`grub-mount {{[-K|--zfs-key]}} /{{path/to/zfs.key}} {{/dev/sdX}} {{/mnt}}`

- 지정한 디버그 범위의 출력 표시:

`grub-mount {{[-d|--debug]}} {{문자열}} {{이미지}} {{/mnt}}`

- 상세 출력 활성화:

`grub-mount {{[-v|--verbose]}} {{이미지}} {{/mnt}}`

- 도움말 표시:

`grub-mount {{[-?|--help]}}`

- 버전 정보 표시:

`grub-mount --version`
