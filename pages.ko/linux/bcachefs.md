# bcachefs

> `bcachefs` 파일 시스템/장치를 관리합니다.
> `device`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
> 더 많은 정보: <https://bcachefs-docs.readthedocs.io/en/latest/index.html>.

- `bcachefs`로 파티션 포맷:

`sudo bcachefs format {{경로/대상/파티션}}`

- `bcachefs` 파일 시스템 마운트:

`sudo bcachefs mount {{경로/대상/파티션}} {{경로/대상/마운트포인트}}`

- SSD를 캐시로, HDD를 장기 저장소로 사용하는 RAID 0 파일 시스템 생성:

`sudo bcachefs format --label=ssd.ssd1 {{경로/대상/ssd/파티션}} --label=hdd.hdd1 {{경로/대상/hdd/파티션}} --replicas=1 --foreground_target=ssd --promote_target=ssd --background_target=hdd`

- 다중 장치 파일 시스템 마운트:

`sudo bcachefs mount {{경로/대상/파티션1}}:{{경로/대상/파티션2}} {{경로/대상/마운트포인트}}`

- 디스크 사용량 표시:

`bcachefs fs usage --human-readable {{경로/대상/마운트포인트}}`

- 포맷 및 마운트 후 복제본 설정:

`sudo bcachefs set-fs-option --metadata_replicas={{2}} --data_replicas={{2}} {{경로/대상/파티션}}`

- 모든 파일이 복제되도록 `bcachefs` 강제화:

`sudo bcachefs data rereplicate {{경로/대상/마운트포인트}}`

- 도움말 표시:

`bcachefs`
