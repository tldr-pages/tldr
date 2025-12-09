# kernel-install

> 커널 및 initrd 이미지를 `/boot`에 추가 및 제거.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/kernel-install.html>.

- 커널 및 initramfs 이미지를 부트로더 파티션에 추가:

`sudo kernel-install add {{커널-버전}} {{커널-이미지}} {{경로/대상/initrd-파일 ...}}`

- 부트로더 파티션에서 커널 제거:

`sudo kernel-install remove {{커널-버전}}`

- 구성되거나 자동으로 감지된 다양한 경로와 매개변수 표시:

`sudo kernel-install inspect {{커널-이미지}}`
