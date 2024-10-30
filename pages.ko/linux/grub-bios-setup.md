# grub-bios-setup

> GRUB을 BIOS 구성으로 사용하는 장치 설정.
> 대부분의 경우 `grub-bios-setup` 대신 `grub-install`을 사용해야 합니다.
> 더 많은 정보: <https://manned.org/grub-bios-setup.8>.

- GRUB으로 부팅하도록 장치 설정:

`grub-bios-setup {{/dev/sdX}}`

- 문제가 감지되어도 설치 강행:

`grub-bios-setup --force {{/dev/sdX}}`

- 특정 디렉터리에 GRUB 설치:

`grub-bios-setup --directory={{/boot/grub}} {{/dev/sdX}}`
