# grub-probe

> 지정한 경로 또는 장치의 장치 정보를 조회.
> 더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dprobe.html>.

- 경로에 해당하는 GRUB 파일 시스템 모듈 조회:

`sudo grub-probe {{[-t|--target]}} fs {{/boot/grub}}`

- 경로가 포함된 시스템 장치 조회:

`sudo grub-probe {{[-t|--target]}} device {{/boot/grub}}`

- 시스템 장치의 GRUB 디스크 이름 조회:

`sudo grub-probe {{[-t|--target]}} drive {{/dev/sdX}} {{[-d|--device]}}`

- 파일 시스템 UUID 조회:

`sudo grub-probe {{[-t|--target]}} fs_uuid {{/boot/grub}}`

- 파일 시스템 레이블 조회:

`sudo grub-probe {{[-t|--target]}} fs_label {{/boot/grub}}`

- MBR 파티션 유형 코드 (16진수 2자리) 조회:

`sudo grub-probe {{[-t|--target]}} msdos_parttype {{/dev/sdX}}`

- 사용자 지정 장치 매핑을 사용해 장치 정보 조회:

`sudo grub-probe {{[-t|--target]}} drive {{/boot/grub}} {{[-m|--device-map]}} {{경로/대상/사용자지정_장치.map}}`
