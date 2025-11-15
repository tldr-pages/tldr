# uncompress

> Unix `compress` 명령으로 압축된 파일을 해제합니다.
> 더 많은 정보: <https://manned.org/uncompress.1>.

- 특정 파일 압축 해제:

`uncompress {{경로/대상/파일1.Z 경로/대상/파일2.Z ...}}`

- 존재하지 않는 파일을 무시하고 특정 파일 압축 해제:

`uncompress -f {{경로/대상/파일1.Z 경로/대상/파일2.Z ...}}`

- `stdout`에 출력 (파일은 변경되지 않고 `.Z` 파일도 생성되지 않음):

`uncompress -c {{경로/대상/파일1.Z 경로/대상/파일2.Z ...}}`

- 자세히 모드 (압축 감소 또는 확장 비율을 `stderr`에 출력):

`uncompress -v {{경로/대상/파일1.Z 경로/대상/파일2.Z ...}}`
