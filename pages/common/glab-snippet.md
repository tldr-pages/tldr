# glab snippet

> Create and manage GitLab snippets.
> More information: <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/snippet/_index.md>.

- Create a new project snippet from a file:

`glab snippet create {{path/to/file}} --title "{{title}}"`

- Create a new personal snippet:

`glab snippet create --personal {{path/to/file}} --title "{{title}}"`

- Create a snippet with a description:

`glab snippet create {{path/to/file}} --title "{{title}}" --description "{{description}}"`

- Create a snippet with a specific visibility level:

`glab snippet create {{path/to/file}} --title "{{title}}" --visibility {{public|internal|private}}`

- Create a snippet from `stdin`:

`echo "{{code}}" | glab snippet create --title "{{title}}" --filename "{{filename}}"`

- Create a snippet for a specific repository:

`glab snippet create --repo {{owner}}/{{repository}} {{path/to/file}} --title "{{title}}"`
