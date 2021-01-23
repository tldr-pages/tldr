# gh secret

> Manage GitHub secrets from the command line.
> More information: <https://cli.github.com/manual/gh_secret>.

- List secret keys for the current repository:

`gh secret list`

- List secret keys for a specific organization:

`gh secret list --org {{organization}}`

- List secret keys for a specific repository:

`gh secret list --repo {{owner}}/{{repository}}`

- Set a secret from a file for the current repository:

`gh secret set {{name}} < {{path/to/file}}`

- Set a secret for a specific repository:

`gh secret set {{name}} --body {{value}} --repo {{owner}}/{{repository}}`

- Set an organization secret for specific repositories:

`gh secret set {{name}} --org {{organization}} --repos {{repository1,repository2}}`

- Remove a secret for the current repository:

`gh secret remove {{name}}`

- Remove a secret for a specific organization:

`gh secret remove {{name}} --org {{organization}}`
