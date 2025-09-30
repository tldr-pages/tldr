# grub-editenv

> GRUB 환경 변수를 편집.
> 더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- 기본 부팅 항목 설정 (부팅 항목이 이미 존재한다고 가정):

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- `timeout` 변수의 현재 값 표시:

`grub-editenv /boot/grub/grubenv list timeout`

- `saved_entry` 변수를 기본값으로 재설정:

`grub-editenv /boot/grub/grubenv unset saved_entry`

- 커널 명령줄에 "quiet splash" 추가:

`grub-editenv /boot/grub/grubenv list kernel_cmdline`
