# hg status

> 작업 디렉토리에서 변경된 파일을 보여줍니다.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/status>.

- 변경된 파일의 상태 표시:

`hg status`

- 수정된 파일만 표시:

`hg status --modified`

- 추가된 파일만 표시:

`hg status --added`

- 제거된 파일만 표시:

`hg status --removed`

- 삭제되었지만 추적된 파일만 표시:

`hg status --deleted`

- 특정 변경 세트와 비교하여 작업 디렉토리의 변경 사항 표시:

`hg status --rev {{리비전}}`

- 특정 글로브 패턴과 일치하는 파일만 표시:

`hg status --include {{패턴}}`

- 특정 글로브 패턴과 일치하지 않는 파일만 표시:

`hg status --exclude {{패턴}}`
