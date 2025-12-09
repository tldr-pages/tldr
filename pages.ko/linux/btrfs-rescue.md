# btrfs rescue

> 손상된 btrfs 파일 시스템 복구 시도.
> 더 많은 정보: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- 파일 시스템 메타데이터 트리 재구성 (매우 느림):

`sudo btrfs rescue chunk-recover {{경로/대상/파티션}}`

- 장치 크기 정렬 관련 문제 해결 (예: 슈퍼 총 바이트 불일치로 파일 시스템을 마운트할 수 없음):

`sudo btrfs rescue fix-device-size {{경로/대상/파티션}}`

- 손상된 슈퍼블록을 올바른 복사본에서 복구 (파일 시스템 트리의 루트 복구):

`sudo btrfs rescue super-recover {{경로/대상/파티션}}`

- 중단된 트랜잭션에서 복구 (로그 재생 문제 수정):

`sudo btrfs rescue zero-log {{경로/대상/파티션}}`

- `mknod`가 설치되지 않은 경우 `/dev/btrfs-control` 제어 장치 생성:

`sudo btrfs rescue create-control-device`
