# argocd

> Interface to control an Argo CD server.
> Some subcommands such as `app` have their own usage documentation.
> More information: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Login to Argo CD server:

`argocd login --insecure --username {{user}} --password {{password}} {{argocd_server:port}}`

- List applications:

`argocd app list`
