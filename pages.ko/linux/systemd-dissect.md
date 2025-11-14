# systemd-dissect

> 파일 시스템 OS 디스크 이미지, 특히 Discoverable Disk Images (DDIs)를 검사하고 상호작용.
> 더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-dissect.html>.

- OS 이미지에 대한 일반 정보 표시:

`systemd-dissect {{경로/대상/image.raw}}`

- OS 이미지 마운트:

`systemd-dissect --mount {{경로/대상/image.raw}} {{/mnt/image}}`

- OS 이미지 언마운트:

`systemd-dissect --umount {{/mnt/image}}`

- 이미지 내 파일 목록 나열:

`systemd-dissect --list {{경로/대상/image.raw}}`

- OS 이미지를 자동으로 할당된 루프백 블록 장치에 연결하고 경로 출력:

`systemd-dissect --attach {{경로/대상/image.raw}}`

- 루프백 블록 장치에서 OS 이미지 분리:

`systemd-dissect --detach {{경로/대상/장치}}`
