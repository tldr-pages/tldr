# jj log

> 리비전 기록을 그래프 형태로 표시.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-log>.

- 리비전 기록을 그래프 형태로 표시:

`jj log`

- 지정한 revset만 표시 (예: `B::D`, `A..D`, `B|C|D` 등):

`jj log {{[-r|--revisions]}} {{revsets}}`

- 각 줄을 지정한 템플릿 형식으로 표시 (예: 커밋 해시 앞 5자리와 작성자):

`jj log {{[-T|--template]}} 'commit_id.shortest(5) ++ " " ++ author'`
