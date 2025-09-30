# pulumi policy

> Manage resource policies on Pulumi Cloud (Business Critical) or locally (no organization sub-commands).
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_policy/>.

- Create a new Pulumi Policy Pack from a template or URL:

`pulumi policy new --dir {{path/to/directory}} {{template|url}}`

- Validate syntax of a policy. To check a policy against a project use `pulumi preview`:

`pulumi policy validate-config {{organization_name}}/{{policy_pack_name}} {{version}}`

- List all policies for an organization:

`pulumi policy ls {{[-j|--json]}} {{organization_name}}`

- Publish a policy to the Pulumi Cloud:

`pulumi policy publish {{organization_name}}`

- Enable a policy with a specific version:

`pulumi policy enable {{organization_name}}/{{policy_pack_name}} {{latest|version}}`

- Disable a policy with a specific version (defaults to all versions):

`pulumi policy disable {{organization_name}}/{{policy_pack_name}} --version {{version}}`

- Display help:

`pulumi policy {{[-h|--help]}}`
