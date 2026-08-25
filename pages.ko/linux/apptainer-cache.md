# apptainer cache

> 로컬 Apptainer 캐시를 관리하는 명령어.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_cache.html>.

- 캐시된 모든 컨테이너 이미지 목록 출력:

`apptainer cache list`

- 상세 정보와 함께 캐시 목록 출력:

`apptainer cache list {{[-v|--verbose]}}`

- 특정 캐시 유형만 출력:

`apptainer cache list {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- 전체 캐시 삭제:

`apptainer cache clean`

- 특정 캐시 유형만 삭제:

`apptainer cache clean {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- 지정한 일수보다 오래된 캐시 항목 삭제:

`apptainer cache clean {{[-D|--days]}} {{일수}}`

- 실제 삭제 없이 삭제 대상 미리보기:

`apptainer cache clean {{[-n|--dry-run]}}`

- 확인 없이 강제로 캐시 삭제:

`apptainer cache clean {{[-f|--force]}}`
