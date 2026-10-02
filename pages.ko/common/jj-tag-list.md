# jj tag list

> `jj` 저장소의 태그를 표시.
> 관련 항목: `jj tag delete`, `jj tag set`.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-list>.

- 모든 태그 목록 표시:

`jj tag {{[l|list]}}`

- 패턴과 일치하는 태그 목록 표시:

`jj tag {{[l|list]}} "{{패턴}}"`

- 부분 문자열 패턴과 일치하는 태그 목록 표시:

`jj tag {{[l|list]}} "{{하위문자열:릴리스}}"`

- 커미터 날짜 기준(최신순)으로 정렬하여 태그 목록 표시:

`jj tag {{[l|list]}} --sort committer-date-`

- 이름 기준 내림차순으로 정렬하여 태그 목록 표시:

`jj tag {{[l|list]}} --sort name-`

- 사용자 지정 템플릿으로 태그 목록 표시:

`jj tag {{[l|list]}} {{[-T|--template]}} "{{템플릿}}"`
