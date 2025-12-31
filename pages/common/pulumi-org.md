# pulumi org

> Manage Pulumi Organization configuration.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_org/>.

- Display the default organization and current backend:

`pulumi org`

- Display the default organization:

`pulumi org get-default`

- Set the default organization:

`pulumi org set-default {{organization_name}}`

- Search for resources in Pulumi Cloud using Pulumi AI with a plaintext natural language query:

`pulumi org search ai {{[-q|--query]}} "{{show me all load balancers in my organization}}"`

- Display help:

`pulumi org {{[-h|--help]}}`
