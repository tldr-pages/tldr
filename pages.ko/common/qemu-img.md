# qemu-img

> Quick Emulator 가상 HDD 이미지를 생성 및 조작.
> 더 많은 정보: <https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- 특정 크기(기가바이트 단위)로 디스크 이미지 생성:

`qemu-img create {{이미지_이름.img}} {{기가바이트}}G`

- 디스크 이미지 정보 표시:

`qemu-img info {{이미지_이름.img}}`

- 이미지 크기 증가 또는 감소:

`qemu-img resize {{이미지_이름.img}} {{기가바이트}}G`

- 지정된 디스크 이미지의 각 섹터 할당 상태 덤프:

`qemu-img map {{이미지_이름.img}}`

- VMware .vmdk 디스크 이미지를 KVM .qcow2 디스크 이미지로 변환:

`qemu-img convert -f {{vmdk}} -O {{qcow2}} {{경로/대상/파일/foo.vmdk}} {{경로/대상/파일/foo.qcow2}}`
