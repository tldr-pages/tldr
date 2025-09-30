# snapper

> 파일 시스템 스냅샷 관리 도구.
> 더 많은 정보: <http://snapper.io/manpages/snapper.html>.

- 스냅샷 구성 목록 나열:

`snapper list-configs`

- 스냅퍼 구성 생성:

`snapper -c {{구성}} create-config {{경로/대상/폴더}}`

- 설명과 함께 스냅샷 생성:

`snapper -c {{구성}} create -d "{{스냅샷_설명}}"`

- 특정 구성의 스냅샷 목록 나열:

`snapper -c {{구성}} list`

- 스냅샷 삭제:

`snapper -c {{구성}} delete {{스냅샷_번호}}`

- 스냅샷 범위 삭제:

`snapper -c {{구성}} delete {{스냅샷1}}-{{스냅샷2}}`
