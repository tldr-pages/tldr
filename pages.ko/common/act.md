# act

> Docker를 사용하여 로컬로 GitHub작업 실행.
> 더 많은 정보: <https://github.com/nektos/act>.

- 가능한 작업들 목록:

`act -l`

- 기본 이벤트 실행:

`act`

- 특정 이벤트 실행:

`act {{event_type}}`

- 특정 작업 실행:

`act -a {{action_id}}`

- 실제론 작업을 실행하지 않기 (예 : a dry run):

`act -n`

- 자세한 로그 표시:

`act -v`

- 특정 워크플로우 실행:

`act push -W {{경로/대상/워크플로우}}`
