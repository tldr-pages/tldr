# dracut

> Linux 커널을 부팅하기 위한 initramfs 이미지를 생성합니다.
> Dracut은 기본적으로 `/etc/dracut.conf`, `/etc/dracut.conf.d/*.conf`, `/usr/lib/dracut/dracut.conf.d/*.conf`의 구성 파일에서 옵션을 사용합니다.
> 더 많은 정보: <https://github.com/dracut-ng/dracut-ng/blob/main/man/dracut.8.adoc>.

- 현재 커널에 대한 initramfs 이미지를 옵션을 덮어쓰지 않고 생성:

`dracut`

- 현재 커널에 대한 initramfs 이미지를 생성하고 기존 이미지를 덮어씀:

`dracut --force`

- 특정 커널에 대한 initramfs 이미지 생성:

`dracut --kver {{커널_버전}}`

- 사용 가능한 모듈 나열:

`dracut --list-modules`
