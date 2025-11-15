# gh project

> Work with GitHub Projects.
> More information: <https://cli.github.com/manual/gh_project>.

- List projects owned by the currently authenticated user:

`gh project {{[ls|list]}}`

- List projects owned by a specific user or organization:

`gh project {{[ls|list]}} --owner {{owner}}`

- View a project by number:

`gh project view {{number}} --owner {{owner}}`

- Create a new project:

`gh project create --owner {{owner}} --title {{project_title}}`

- Add an item (issue or pull request) to a project:

`gh project item-add {{number}} --owner {{owner}} --url {{issue_or_pr_url}}`

- List items in a project:

`gh project item-list {{number}} --owner {{owner}}`

- Close a project:

`gh project close {{number}} --owner {{owner}}`
