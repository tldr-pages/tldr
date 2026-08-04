# jira

> Jira와 상호작용하기 위한 서드파티 CLI.
> 참고: Jira API 토큰을 발급받아 쉘의 `$JIRA_API_TOKEN` 환경 변수로 설정해야 함.
> 더 많은 정보: <https://github.com/ankitpokhrel/jira-cli#commands>.

- 설정 파일 생성 (`jira` 사용 전 필수 사항):

`jira init`

- 최근 이슈 목록 표시:

`jira issue {{[ls|list]}}`

- 담당자가 없고 우선순위가 높은 이슈 목록 표시:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} x {{[-y|--priority]}} High`

- 현재 스프린트에서 나에게 할당된 이슈 목록 표시:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- 상위 이슈를 지정하여 새로운 이슈 생성:

`jira issue create {{[-P|--parent]}} {{상위_이슈}}`

- 브라우저에서 이슈 열기:

`jira open {{123}}`
