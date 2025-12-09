# jira sprint

> Manage sprints in a Jira project board.
> More information: <https://github.com/ankitpokhrel/jira-cli#sprint>.

- List sprints in an explorer view:

`jira sprint {{[ls|list]}}`

- List issues from the current sprint:

`jira sprint {{[ls|list]}} --current`

- List issues from the current sprint, assigned to me:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- List high priority issues from the current sprint assigned to me:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Add issues to a sprint using an interactive prompt:

`jira sprint add`
