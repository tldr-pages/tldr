# helm rollback

> Roll back a helm release to a previous revision.
> More information: <https://helm.sh/docs/helm/helm_rollback/>.

- Roll back a release to its previous revision:

`helm rollback {{release_name}}`

- Roll back a release to a specific revision:

`helm rollback {{release_name}} {{revision}}`

- Roll back a release in a specific namespace:

`helm rollback {{release_name}} {{revision}} {{[-n|--namespace]}} {{namespace}}`

- Simulate a rollback without actually doing it:

`helm rollback {{release_name}} {{revision}} --dry-run`

- Roll back a release and wait until its resources are ready:

`helm rollback {{release_name}} {{revision}} --wait`

- Delete resources created by the rollback if it fails:

`helm rollback {{release_name}} {{revision}} --cleanup-on-fail`

- Roll back a release without running hooks:

`helm rollback {{release_name}} {{revision}} --no-hooks`
