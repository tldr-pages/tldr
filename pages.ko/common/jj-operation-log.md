# jj operation log

> `jj` 저장소의 작업 로그를 표시.
> 더 많은 정보: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-log>.

- 작업 로그 표시:

`jj {{[op|operation]}} log`

- 표시할 작업 수 제한:

`jj {{[op|operation]}} log {{[-n|--limit]}} {{개수}}`

- 작업을 역순으로 표시 (오래된 작업먼저):

`jj {{[op|operation]}} log --reversed`

- 그래프 없이 작업 로그 표시:

`jj {{[op|operation]}} log {{[-G|--no-graph]}}`

- 사용자 지정 템플릿을 사용하여 작업 로그 표시:

`jj {{[op|operation]}} log {{[-T|--template]}} "{{템플릿}}"`
