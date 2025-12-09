# bd

> A lightweight memory system and git-backed issue tracker for AI coding agents.
> More information: <https://github.com/steveyegge/beads#usage>.

- Initialize a project database:

`bd init`

- Create a new issue with description, priority, and type:

`bd create {{issue_title}} {{[-d|--description]}} {{description}} {{[-p|--priority]}} {{1}} {{[-t|--type]}} {{bug}}`

- List all issues:

`bd list`

- Show issues ready to work on (no blockers):

`bd ready`

- Display details of a specific issue:

`bd show {{issue_id}}`

- Update an issue status:

`bd update {{issue_id}} --status {{in_progress|completed|blocked}}`

- Manually sync changes and import latest from git:

`bd sync`

- Display help:

`bd {{[-h|--help]}}`
