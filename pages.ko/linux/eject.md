# eject

> CD, 플로피 디스크 및 테이프 드라이브를 꺼냅니다.
> 더 많은 정보: <https://manned.org/eject>.

- 기본 장치 표시:

`eject -d`

- 기본 장치 꺼내기:

`eject`

- 특정 장치 꺼내기 (기본 순서는 cd-rom, scsi, 플로피 및 테이프입니다):

`eject {{/dev/cdrom}}`

- 장치 트레이가 열려 있는지 닫혀 있는지 토글:

`eject -T {{/dev/cdrom}}`

- CD 드라이브 꺼내기:

`eject -r {{/dev/cdrom}}`

- 플로피 드라이브 꺼내기:

`eject -f {{/mnt/floppy}}`

- 테이프 드라이브 꺼내기:

`eject -q {{/mnt/tape}}`
