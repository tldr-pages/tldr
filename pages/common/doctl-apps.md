# doctl apps

> Manage DigitalOcean apps.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

- Create an app:

`doctl {{[a|apps]}} {{[c|create]}}`

- Create a deployment for a specific app:

`doctl {{[a|apps]}} {{[cd|create-deployment]}} {{app_id}}`

- Delete an app interactively:

`doctl {{[a|apps]}} {{[d|delete]}} {{app_id}}`

- Get an app:

`doctl {{[a|apps]}} {{[g|get]}}`

- List all apps:

`doctl {{[a|apps]}} {{[ls|list]}}`

- List all deployments from a specific app:

`doctl {{[a|apps]}} {{[lsd|list-deployments]}} {{app_id}}`

- Get logs from a specific app:

`doctl {{[a|apps]}} {{[l|logs]}} {{app_id}}`

- Update a specific app with a given app spec:

`doctl {{[a|apps]}} {{[u|update]}} {{app_id}} --spec {{path/to/spec.yml}}`
