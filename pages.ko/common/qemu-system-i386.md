# qemu-system-i386

> `i386` 아키텍처를 에뮬레이션.
> 더 많은 정보: <https://www.qemu.org/docs/master/system/target-i386.html>.

- 디스크 이미지를 사용하여 `i386` 아키텍처 부팅:

`qemu-system-i386 -hda {{이미지_이름.img}} -m {{4096}}`

- 라이브 ISO 이미지로 QEMU 인스턴스 부팅:

`qemu-system-i386 -hda {{이미지_이름.img}} -m {{4096}} -cdrom {{os_이미지.iso}} -boot d`

- 물리적 저장 장치에서 부팅 (예: USB에서 부팅하여 부팅 가능한 미디어를 테스트):

`qemu-system-i386 -hda {{/dev/저장_장치}} -m {{4096}}`

- VNC 서버 없이 실행:

`qemu-system-i386 -hda {{이미지_이름.img}} -m {{4096}} -nographic`

- 비그래픽 모드의 QEMU 종료:

`<Ctrl a><x>`

- 지원되는 머신 타입 목록 표시:

`qemu-system-i386 {{[-M|-machine]}} help`
