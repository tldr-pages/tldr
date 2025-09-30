# glab mr create

> Manage GitLab merge requests.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/mr/create.md>.

- Interactively create a merge request:

`glab mr create`

- Create a merge request, determining the title and description from the commit messages of the current branch:

`glab mr create {{[-f|--fill]}}`

- Create a draft merge request:

`glab mr create --draft`

- Create a merge request specifying the target branch, title, and description:

`glab mr create {{[-b|--target-branch]}} {{target_branch}} {{[-t|--title]}} "{{title}}" {{[-d|--description]}} "{{description}}"`

- Start opening a merge request in the default web browser:

`glab mr create {{[-w|--web]}}`
