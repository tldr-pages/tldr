# smartctl

> 디스크 상태를 SMART 데이터를 통해 모니터링.
> 더 많은 정보: <https://www.smartmontools.org>.

- SMART 건강 요약 표시:

`sudo smartctl --health {{/dev/sdX}}`

- 장치 정보 표시:

`sudo smartctl --info {{/dev/sdX}}`

- 백그라운드에서 짧은 자체 테스트 시작:

`sudo smartctl --test short {{/dev/sdX}}`

- 현재/마지막 자체 테스트 상태 및 기타 SMART 기능 표시:

`sudo smartctl --capabilities {{/dev/sdX}}`

- 포괄적인 SMART 데이터 표시:

`sudo smartctl --all {{/dev/sdX}}`
