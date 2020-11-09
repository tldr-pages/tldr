# vela

> Command line tools for Vela pipeline.
> More information: <https://go-vela.github.io/docs/cli/>.

- Trigger pipeline to run from git tagged version:

`vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch, commit, or refs/tags/git_tag}} --description "{{deploy_description}}"`
