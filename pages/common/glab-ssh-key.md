# glab ssh-key

> Manage SSH keys for a GitLab account.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/ssh-key/_index.md>.

- List SSH keys for the currently authenticated user:

`glab ssh-key list`

- List SSH keys including their numeric IDs:

`glab ssh-key list --show-id`

- Add an SSH key from a public key file with a title:

`glab ssh-key add {{path/to/key.pub}} {{[-t|--title]}} "{{title}}"`

- Add an SSH key from `stdin` with a title:

`glab ssh-key add {{[-t|--title]}} "{{title}}"`

- Add an SSH key with a specific usage type (defaults to `auth_and_signing`):

`glab ssh-key add {{path/to/key.pub}} {{[-t|--title]}} "{{title}}" {{[-u|--usage-type]}} {{auth|signing|auth_and_signing}}`

- Add an SSH key with an expiration date (ISO 8601 format):

`glab ssh-key add {{path/to/key.pub}} {{[-t|--title]}} "{{title}}" {{[-e|--expires-at]}} "{{YYYY-MM-DD}}"`

- View details of a specific SSH key by its numeric ID:

`glab ssh-key get {{key_id}}`

- Delete an SSH key from the authenticated user's account by its numeric ID:

`glab ssh-key delete {{key_id}}`
