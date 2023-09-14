# linode-cli nodebalancers

> Command-line interface to manage Linode NodeBalancers via `linode-cli`.

- List all NodeBalancers:

`linode-cli nodebalancers list`

- Create a new NodeBalancer:

`linode-cli nodebalancers create --region [region]`

- View details of a specific NodeBalancer:

`linode-cli nodebalancers view [nodebalancer-id]`

- Update an existing NodeBalancer:

`linode-cli nodebalancers update [nodebalancer-id] --label [new-label]`

- Delete a NodeBalancer:

`linode-cli nodebalancers delete [nodebalancer-id]`

- List configurations for a NodeBalancer:

`linode-cli nodebalancers configs list [nodebalancer-id]`

- Add a new configuration to a NodeBalancer:

`linode-cli nodebalancers configs create [nodebalancer-id] --port [port] --protocol [protocol]`
