# jira issue

> Jira 프로젝트의 이슈를 관리.
> 더 많은 정보: <https://github.com/ankitpokhrel/jira-cli#issue>.

- 최근 이슈 목록 표시:

`jira issue {{[ls|list]}}`

- 지정한 사용자에게 할당된 이슈 목록 표시:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} "{{이메일_또는_표시_이름}}"`

- 나에게 할당된 높은 우선순위의 이슈 목록 표시:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- 대화형 프롬프트를 사용하여 이슈 생성:

`jira issue create`

- 대화형 프롬프트를 사용하여 이슈 수정:

`jira issue edit`

- 대화형 프롬프트를 사용하여 사용자에게 이슈 할당:

`jira issue {{[asg|assign]}}`

- 이슈를 지정한 상태로 변경:

`jira issue {{[mv|move]}} {{이슈_아이디}} "{{In Progress}}"`

- 터미널에서 `less`를 사용하여 이슈 보기:

`jira issue view {{이슈_아이디}}`
