# glab label

> Manage labels for GitLab repositories and groups.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/label/_index.md>.

- List labels for the current repository:

`glab label {{[ls|list]}}`

- List labels for a specific repository:

`glab label list {{[-R|--repo]}} {{owner}}/{{repository}}`

- List labels for a specific group:

`glab label list {{[-g|--group]}} {{group_name}}`

- Create a new label with a name and color (name or hex code, defaults to `#428BCA`):

`glab label create {{[-n|--name]}} {{name}} {{[-c|--color]}} "{{color}}"`

- Create a new label with a description:

`glab label create {{[-n|--name]}} {{name}} {{[-d|--description]}} "{{description}}"`

- Update a label's name and description by its numeric ID:

`glab label edit {{[-l|--label-id]}} {{label_id}} {{[-n|--new-name]}} {{new_name}} {{[-d|--description]}} "{{description}}"`

- Delete a label from the current repository:

`glab label delete {{name}}`
