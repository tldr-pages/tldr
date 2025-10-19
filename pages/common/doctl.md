# doctl

> Official command-line interface for the DigitalOcean API.
> Manage Droplets, Kubernetes, App Platform, databases, billing, and more.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/>.

- Authenticate the CLI using a personal access token:

`doctl auth init --access-token {{token}}`

- Show your account information:

`doctl account get`

- List Droplets (virtual machines):

`doctl compute droplet list`

- Create a Droplet and wait for it to become active:

`doctl compute droplet create {{name}} --region {{nyc3}} --image {{ubuntu-24-04-x64}} --size {{s-1vcpu-1gb}} --ssh-keys {{fingerprint_or_id}} --wait`

- List Kubernetes clusters:

`doctl kubernetes cluster list`

- Save a kubeconfig for a cluster to use with kubectl:

`doctl kubernetes cluster kubeconfig save {{cluster_name}}`

- Create a Kubernetes cluster with a node pool and wait:

`doctl kubernetes cluster create {{name}} --region {{nyc3}} --version {{latest}} --node-pool "name={{pool_name}},size={{s-2vcpu-2gb}},count={{3}}" --wait`

- List App Platform apps:

`doctl apps list`
