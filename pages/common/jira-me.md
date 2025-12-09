# jira me

> Display the configured `jira` user.
> More information: <https://github.com/ankitpokhrel/jira-cli#issue>.

- Display the configured `jira` user:

`jira me`

- List issues assigned to me:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me)`

- List issues from the current sprint, assigned to me:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Display help:

`jira me {{[-h|--help]}}`
