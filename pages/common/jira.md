# jira

> Interface (third party) for interacting with Jira.
> Note: Obtaining a Jira API token and exporting it to the shell as a `JIRA_API_TOKEN` variable is required.
> More information: <https://github.com/ankitpokhrel/jira-cli#commands>.

- Create a configuration file (required before using `jira`):

`jira init`

- List recent issues:

`jira issue {{[ls|list]}}`

- List unassigned issues with high priority:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} x {{[-y|--priority]}} "High"`

- List issues from the current sprint, assigned to me:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Create a new issue with a parent issue:

`jira issue create {{[-P|--parent]}} {{parent}}`

- Open an issue in the browser:

`jira open {{123}}`
