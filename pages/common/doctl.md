# doctl

> Manage DigitalOcean resources.
> More information: <https://docs.digitalocean.com/reference/doctl/>.

- Authenticate with DigitalOcean:

`doctl auth init`

- Display account information:

`doctl account get`

- Create a new Droplet:

`doctl compute droplet create {{name}} --size {{size}} --image {{image}} --region {{region}}`

- List all Droplets:

`doctl compute droplet list`

- SSH into a Droplet:

`doctl compute ssh {{droplet_id}}`

- Create a Kubernetes cluster:

`doctl kubernetes cluster create {{cluster_name}}`

- List Kubernetes clusters:

`doctl kubernetes cluster list`

- List managed databases:

`doctl databases list`
