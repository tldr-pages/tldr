# vela

> Command line tools for the Vela pipeline.
> More information: <https://go-vela.github.io/docs/cli/>.

- Trigger a pipeline to run from a Git branch, commit or tag:

`vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch|commit|refs/tags/git_tag}} --description "{{deploy_description}}"`

- List deployments for a repository:

`vela get deployment --org {{organization}} --repo {{repository_name}}`

- Inspect a specific deployment:

`vela view deployment --org {{organization}} --repo {{repository_name}} --deployment {{deployment_number}}`
