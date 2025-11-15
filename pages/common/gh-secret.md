# gh secret

> Manage GitHub secrets.
> More information: <https://cli.github.com/manual/gh_secret>.

- List secret keys for the current repository:

`gh secret {{[ls|list]}}`

- List secret keys for a specific organization:

`gh secret {{[ls|list]}} {{[-o|--org]}} {{organization}}`

- List secret keys for a specific repository:

`gh secret {{[ls|list]}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Set a secret for the current repository (user will be prompted for the value):

`gh secret set {{name}}`

- Set a secret from a file for the current repository:

`gh < {{path/to/file}} secret set {{name}}`

- Set an organization secret for specific repositories:

`gh secret set {{name}} {{[-o|--org]}} {{organization}} {{[-r|--repos]}} {{repository1,repository2}}`

- Remove a secret for the current repository:

`gh secret remove {{name}}`

- Remove a secret for a specific organization:

`gh secret remove {{name}} {{[-o|--org]}} {{organization}}`
