# jira issue

> Manage issues in a Jira project.
> More information: <https://github.com/ankitpokhrel/jira-cli#issue>.

- List recent issues:

`jira issue {{[ls|list]}}`

- List issues assigned to a specific user:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} "{{email_or_display_name}}"`

- List high priority issues assigned to me:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Create an issue using an interactive prompt:

`jira issue create`

- Edit an issue using an interactive prompt:

`jira issue edit`

- Assign user to an issue using an interactive prompt:

`jira issue {{[asg|assign]}}`

- Move an issue to a certain state:

`jira issue {{[mv|move]}} {{issue_id}} "{{In Progress}}"`

- Open an issue in the terminal using `less`:

`jira issue view {{issue_id}}`
