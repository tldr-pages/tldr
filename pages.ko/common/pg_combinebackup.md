# pg_combinebackup

> 증분 백업 체인을 사용하여 전체 (합성) PostgreSQL 백업을 재구성.
> 여러 백업을 지정할 경우 가장 오래된 백업부터 최신 백업 순으로 지정해야 함.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-pgcombinebackup.html>.

- 전체 백업과 증분 백업을 하나의 합성 전체 백업으로 결합:

`pg_combinebackup {{경로/대상/전체_백업}} {{경로/대상/증분_백업}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- dry run 수행(실제 파일을 생성하지 않고 수행 예정 작업만 표시):

`pg_combinebackup {{[-n|--dry-run]}} {{경로/대상/전체_백업}} {{경로/대상/증분_백업}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- 파일 복사 대신 하드 링크 사용 (더 빠르며, 동일한 파일 시스템 필요):

`pg_combinebackup {{[-k|--link]}} {{경로/대상/전체_백업}} {{경로/대상/증분_백업}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- 지원되는 경우 파일 복제 (reflink)를 사용하여 효율적으로 복사:

`pg_combinebackup --clone {{경로/대상/전체_백업}} {{경로/대상/증분_백업}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- `copy_file_range` 시스템 호출을 사용하여 효율적으로 복사:

`pg_combinebackup --copy-file-range {{경로/대상/전체_백업}} {{경로/대상/증분_백업}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- 재구성 중 tablespace 위치 변경:

`pg_combinebackup {{경로/대상/백업1 경로/대상/백업2 ...}} {{[-T|--tablespace-mapping]}} /{{경로/대상/오래된_tablespace}}=/{{경로/대상/새로운_tablespace}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- 더 빠르지만 안전하지 않은 쓰기를 위해 fsync 비활성화 (테스트 전용):

`pg_combinebackup {{[-N|--no-sync]}} {{경로/대상/백업1 경로/대상/백업2 ...}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`

- 상세한 디버그 출력 표시:

`pg_combinebackup {{[-d|--debug]}} {{경로/대상/백업1 경로/대상/백업2 ...}} {{[-o|--output]}} {{경로/대상/출력_디렉터리}}`
