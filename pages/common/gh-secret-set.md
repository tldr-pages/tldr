# gh secret set

> Create or update GitHub secrets.
> More information: <https://cli.github.com/manual/gh_secret_set>.

- Set a secret for the current repository (user will be prompted for the value):

`gh secret set {{name}}`

- Set a secret from a file for the current repository:

`gh < {{path/to/file}} secret set {{name}}`

- Set a secret for a specific repository:

`gh secret set {{name}} {{[-b|--body]}} {{value}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Set an organization secret for specific repositories:

`gh secret set {{name}} {{[-o|--org]}} {{organization}} {{[-r|--repos]}} "{{repository1,repository2,...}}"`

- Set an organization secret with a specific visibility:

`gh secret set {{name}} {{[-o|--org]}} {{organization}} {{[-v|--visibility]}} {{all|private|selected}}`
