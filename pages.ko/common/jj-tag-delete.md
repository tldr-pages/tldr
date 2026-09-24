# jj tag delete

> `jj` 저장소의 태그를 삭제.
> 관련 항목: `jj tag list`, `jj tag set`.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-delete>.

- 태그 삭제:

`jj tag {{[d|delete]}} {{태그_이름}}`

- 여러 태그 삭제:

`jj tag {{[d|delete]}} {{태그1 태그2 ...}}`

- glob 패턴과 일치하는 태그 삭제:

`jj tag {{[d|delete]}} "{{glob:v1.*}}"`

- 부분 문자열 패턴과 일치하는 태그 삭제:

`jj tag {{[d|delete]}} "{{하위문자열:릴리스}}"`

- 정확한 이름으로 태그 삭제:

`jj tag {{[d|delete]}} "{{exact:v1.0.0}}"`
