# jira

> Interface (third party) for interacting with Jira.
> More information: <https://github.com/ankitpokhrel/jira-cli>.

- List recent issues:

`jira issue list`

- List issues from the current sprint, assigned to me:

`jira sprint list --current {{[-a|--assignee]}} $(jira me)`

- Create a new issue, optionally set a parent issue:

`jira issue create {{[-P|--parent]}} {{parent}}`
