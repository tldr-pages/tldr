# jira me

> 현재 설정된 `jira` 사용자를 표시.
> 더 많은 정보: <https://github.com/ankitpokhrel/jira-cli#commands>.

- 현재 설정된 `jira` 사용자 표시:

`jira me`

- 나에게 할당된 이슈 목록 표시:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me)`

- 현재 스프린트에서, 나에게 할당된 이슈 목록 표시:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- 도움말 표시:

`jira me {{[-h|--help]}}`
