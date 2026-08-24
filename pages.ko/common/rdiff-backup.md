# rdiff-backup

> 로컬/원격 미러링 및 증분 백업 도구.
> 더 많은 정보: <https://rdiff-backup.net/rdiff-backup.1.html>.

- `path/to/source`를 `경로/대상/백업`에 백업:

`rdiff-backup backup {{path/to/source}} {{경로/대상/백업}}`

- 저장소(로컬 또는 원격)의 증분 백업 목록 표시:

`rdiff-backup list increments {{저장소}}`

- 가장 최근 백업에서 복원:

`rdiff-backup restore {{경로/대상/백업}} {{경로/대상/목적지}}`

- 3일 전 시점의 백업 파일 복원:

`rdiff-backup restore --at 3D {{경로/대상/백업}} {{경로/대상/목적지}}`
