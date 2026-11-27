# glab variable

> Manage variables for a GitLab project or group.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/variable/_index.md>.

- List variables for the current project:

`glab variable list`

- List variables for a specific GitLab group:

`glab variable list {{[-g|--group]}} {{group_name}}`

- Display the value of a specific variable:

`glab variable get {{key}}`

- Set a project variable:

`glab variable set {{key}} "{{value}}"`

- Set a masked and protected variable for a specific environment scope:

`glab variable set {{key}} "{{value}}" {{[-m|--masked]}} {{[-p|--protected]}} {{[-s|--scope]}} "{{scope}}"`

- Set a variable with a specific type (defaults to `env_var`):

`glab variable set {{key}} "{{value}}" {{[-t|--type]}} {{env_var|file}}`

- Export project variables as `KEY=VALUE` pairs:

`glab variable export {{[-F|--output]}} env`

- Delete a project variable:

`glab variable delete {{key}}`
