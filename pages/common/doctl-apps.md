# doctl apps

> Used to manage digitalocean apps.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

- Create an app:

`doctl apps create`

- Create a deployment for a specific app:

`doctl apps create-deployment {{app_id}}`

- Delete an app interactively:

`doctl apps delete {{app_id}}`

- Get an app:

`doctl apps get`

- List all apps:

`doctl apps list`

- List all deployments from a specific app:

`doctl apps list-deployments {{app_id}}`

- Get logs from a specific app:

`doctl apps logs {{app_id}}`

- Update a specific app with a given app spec:

`doctl apps update {{app_id}} --spec {{path/to/spec.yml}}`
