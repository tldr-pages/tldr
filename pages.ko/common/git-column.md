# git column

> 데이터를 여러 열로 표시.
> 더 많은 정보: <https://git-scm.com/docs/git-column>.

- `stdin`을 여러 열로 형식화:

`ls | git column --mode={{column}}`

- 최대 너비가 `100`인 여러 열로 `stdin`을 형식화:

`ls | git column --mode=column --width={{100}}`

- 최대 여백이 `30`인 여러 열로 `stdin`을 형식화:

`ls | git column --mode=column --padding={{30}}`
