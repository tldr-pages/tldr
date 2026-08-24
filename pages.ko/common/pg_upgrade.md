# pg_upgrade

> PostgreSQL 데이터베이스 클러스터를 새로운 메이저 버전으로 업그레이드.
> 더 많은 정보: <https://www.postgresql.org/docs/current/pgupgrade.html>.

- 업그레이드 전에 클러스터 검사:

`pg_upgrade {{[-c|--check]}} {{[-b|--old-bindir]}} {{경로/대상/오래된_bin}} {{[-B|--new-bindir]}} {{경로/대상/새로운_bin}} {{[-d|--old-datadir]}} {{경로/대상/오래된_데이터}} {{[-D|--new-datadir]}} {{경로/대상/새로운_데이터}}`

- 실제 업그레이드 수행:

`pg_upgrade {{[-b|--old-bindir]}} {{경로/대상/오래된_bin}} {{[-B|--new-bindir]}} {{경로/대상/새로운_bin}} {{[-d|--old-datadir]}} {{경로/대상/오래된_데이터}} {{[-D|--new-datadir]}} {{경로/대상/새로운_데이터}}`

- 업그레이드 중 여러 병렬 작업 사용:

`pg_upgrade {{[-j|--jobs]}} {{여러_jobs}} {{[-b|--old-bindir]}} {{경로/대상/오래된_bin}} {{[-B|--new-bindir]}} {{경로/대상/새로운_bin}} {{[-d|--old-datadir]}} {{경로/대상/오래된_데이터}} {{[-D|--new-datadir]}} {{경로/대상/새로운_데이터}}`

- 기존 및 새로운 PostgreSQL 포트 지정:

`pg_upgrade {{[-p|--old-port]}} {{port}} {{[-P|--new-port]}} {{port}} {{[-b|--old-bindir]}} {{경로/대상/오래된_bin}} {{[-B|--new-bindir]}} {{경로/대상/새로운_bin}} {{[-d|--old-datadir]}} {{경로/대상/오래된_데이터}} {{[-D|--new-datadir]}} {{경로/대상/새로운_데이터}}`

- 새로운 클러스터로 파일을 복사하는 대신 하드 링크 사용:

`pg_upgrade {{[-k|--link]}} {{[-b|--old-bindir]}} {{경로/대상/오래된_bin}} {{[-B|--new-bindir]}} {{경로/대상/새로운_bin}} {{[-d|--old-datadir]}} {{경로/대상/오래된_데이터}} {{[-D|--new-datadir]}} {{경로/대상/새로운_데이터}}`

- 도움말 표시:

`pg_upgrade {{[-?|--help]}}`
