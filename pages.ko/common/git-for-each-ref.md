# git for-each-ref

> Git 저장소의 참조(ref: 브랜치, 태그 등) 목록 표시 및 형식 지정.
> 더 많은 정보: <https://git-scm.com/docs/git-for-each-ref>.

- 모든 ref(브랜치와 태그) 목록 표시:

`git for-each-ref`

- 브랜치만 목록 표시:

`git for-each-ref refs/heads/`

- 태그만 목록 표시:

`git for-each-ref refs/tags/`

- `HEAD`에 병합된 브랜치 목록 표시:

`git for-each-ref --merged HEAD refs/heads/`

- 모든 ref의 짧은 이름 표시:

`git for-each-ref --format "%(refname:short)"`

- 커미터 날짜 기준으로 최신순 정렬:

`git for-each-ref --sort -committerdate`

- 커미터 날짜 기준으로 오래된순 정렬:

`git for-each-ref --sort committerdate`

- 지정한 개수만큼만 ref 출력:

`git for-each-ref --count {{숫자}}`
