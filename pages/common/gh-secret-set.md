# gh secret set

> Create or update GitHub secrets from the command-line.
> More information: <https://cli.github.com/manual/gh_secret_set>.

- Set a secret for the current repository (user will be prompted for the value):

`gh secret set {{name}}`

- Set a secret from a file for the current repository:

`gh secret set {{name}} < {{path/to/file}}`

- Set a secret for a specific repository:

`gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}`

- Set an organization secret for specific repositories:

`gh secret set {{name}} --org {{organization}} --repos "{{repository1,repository2,...}}"`

- Set an organization secret with a specific visibility:

`gh secret set {{name}} --org {{organization}} --visibility {{all|private|selected}}`
