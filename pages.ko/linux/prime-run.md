# prime-run

> 대체 Nvidia 그래픽 카드를 사용하여 프로그램을 실행합니다.
> 더 많은 정보: <https://wiki.archlinux.org/title/PRIME#PRIME_render_offload>.

- 전용 Nvidia GPU를 사용하여 프로그램 실행:

`prime-run {{명령어}}`

- Nvidia 카드가 사용되고 있는지 확인:

`prime-run glxinfo | grep "OpenGL renderer"`
