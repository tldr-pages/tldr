# poetry remove

> 프로젝트 의존성에서 패키지를 제거.
> 더 많은 정보: <https://python-poetry.org/docs/cli/#remove>.

- 프로젝트 의존성에서 하나 이상의 패키지 제거:

`poetry remove {{패키지1 패키지2 ...}}`

- 개발 의존성에서 패키지 제거:

`poetry remove {{패키지}} {{[-D|--dev]}}`

- 지정한 의존성 그룹에서 패키지 제거:

`poetry remove {{패키지}} {{[-G|--group]}} {{그룹_이름}}`

- 실제 변경 없이 패키지 제거 결과 미리 확인 (dry-run):

`poetry remove {{패키지}} --dry-run`

- 현재 환경에서 패키지 제거 없이 잠금 파일만 업데이트:

`poetry remove {{패키지}} --lock`
