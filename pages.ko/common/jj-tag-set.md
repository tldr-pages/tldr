# jj tag set

> `jj` 저장소의 태그를 생성하거나 업데이트.
> 관련 항목: `jj tag delete`, `jj tag list`.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-tag-set>.

- 현재 작업 복사본 리비전을 가리키는 태그 생성:

`jj tag {{[s|set]}} {{태그_이름}}`

- 지정한 리비전을 가리키는 태그 생성:

`jj tag {{[s|set]}} {{태그_이름}} {{[-r|--revision]}} {{revision}}`

- 동일한 리비전을 가리키는 여러 태그 생성:

`jj tag {{[s|set]}} {{태그1 태그2 ...}} {{[-r|--revision]}} {{revision}}`

- 기존 태그를 다른 리비전으로 이동:

`jj tag {{[s|set]}} {{태그_이름}} {{[-r|--revision]}} {{revision}} --allow-move`

- 현재 리비전의 부모를 가리키는 태그 생성:

`jj tag {{[s|set]}} {{태그_이름}} {{[-r|--revision]}} @-`
