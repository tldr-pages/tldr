# hg log

> 저장소의 수정 내역을 표시.
> 더 많은 정보: <https://www.mercurial-scm.org/help/commands/log>.

- 저장소의 전체 수정 내역 표시:

`hg log`

- ASCII 그래프와 함께 수정 내역 표시:

`hg log {{[-G|--graph]}}`

- 지정된 패턴과 일치하는 파일 이름과 함께 수정 내역 표시:

`hg log {{[-I|--include]}} {{패턴}}`

- 지정된 패턴과 일치하는 파일 이름을 제외한 수정 내역 표시:

`hg log {{[-X|--exclude]}} {{패턴}}`

- 특정 수정에 대한 로그 정보 표시:

`hg log {{[-r|--rev]}} {{수정}}`

- 특정 브랜치의 수정 내역 표시:

`hg log {{[-b|--branch]}} {{브랜치}}`

- 특정 날짜에 대한 수정 내역 표시:

`hg log {{[-d|--date]}} {{날짜}}`

- 특정 사용자에 의해 커밋된 수정 내역 표시:

`hg log {{[-u|--user]}} {{사용자}}`
