# linode-cli nodebalancers

> Manage Linode NodeBalancers.
> See also: `linode-cli`.
> More information: <https://www.linode.com/docs/products/tools/cli/guides/nodebalancers/>.

- List all NodeBalancers:

`linode-cli nodebalancers list`

- Create a new NodeBalancer:

`linode-cli nodebalancers create --region {{region}}`

- View details of a specific NodeBalancer:

`linode-cli nodebalancers view {{nodebalancer_id}}`

- Update an existing NodeBalancer:

`linode-cli nodebalancers update {{nodebalancer_id}} --label {{new_label}}`

- Delete a NodeBalancer:

`linode-cli nodebalancers delete {{nodebalancer_id}}`

- List configurations for a NodeBalancer:

`linode-cli nodebalancers configs list {{nodebalancer_id}}`

- Add a new configuration to a NodeBalancer:

`linode-cli nodebalancers configs create {{nodebalancer_id}} --port {{port}} --protocol {{protocol}}`
