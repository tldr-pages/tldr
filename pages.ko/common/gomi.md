# gomi

> 휴지통 관리 도구.
> 관련 항목: `trash`, `rm`.
> 더 많은 정보: <https://github.com/babarot/gomi>.

- 특정 파일 또는 폴더를 안전하게 삭제:

`gomi {{경로/대상/파일1 경로/대상/파일2 경로/대상/폴더1 경로/대상/폴더2 ...}}`

- 하나 이상의 파일을 복원할 수 있는 대화형 메뉴 열기:

`gomi {{[-b|--restore]}}`

- 지정한 기간보다 오래된 휴지통 파일 삭제 (일([d]ay), 주([w]eek), 월([m]onth), 년([y]ear)):

`gomi --prune {{1d|1w|1m|1y|...}}`

- 고아 상태의 `.trashinfo` 파일 삭제:

`gomi --prune {{고아_파일}}`
