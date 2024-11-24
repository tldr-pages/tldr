# qemu

> 범용 머신 에뮬레이터 및 가상화 도구.
> 다양한 CPU 아키텍처를 지원.
> 더 많은 정보: <https://www.qemu.org>.

- i386 아키텍처를 에뮬레이트하여 이미지에서 부팅:

`qemu-system-i386 -hda {{이미지_이름.img}}`

- x64 아키텍처를 에뮬레이트하여 이미지에서 부팅:

`qemu-system-x86_64 -hda {{이미지_이름.img}}`

- 라이브 ISO 이미지를 사용하여 QEMU 인스턴스 부팅:

`qemu-system-i386 -hda {{이미지_이름.img}} -cdrom {{os_이미지.iso}} -boot d`

- 인스턴스에 할당할 RAM의 양 지정:

`qemu-system-i386 -m 256 -hda {{이미지_이름.img}} -cdrom {{os_이미지.iso}} -boot d`

- 물리적 장치에서 부팅 (예: 부팅 가능한 매체 테스트를 위한 USB):

`qemu-system-i386 -hda {{/dev/저장장치}}`
