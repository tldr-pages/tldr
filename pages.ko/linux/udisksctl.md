# udisksctl

> `udisksd`와 상호 작용하여 스토리지 장치를 조회하고 조작.
> 더 많은 정보: <https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- 디스크 드라이브 및 블록 장치에 대한 상위 정보 표시:

`udisksctl status`

- 장치에 대한 자세한 정보 표시:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdX}}`

- 장치 파티션에 대한 자세한 정보 표시:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdXN}}`

- 장치 파티션을 마운트하고 마운트 지점을 출력:

`udisksctl mount {{[-b|--block-device]}} {{/dev/sdXN}}`

- 장치 파티션을 마운트 해제:

`udisksctl unmount {{[-b|--block-device]}} {{/dev/sdXN}}`

- 데몬의 이벤트 모니터링:

`udisksctl monitor`
