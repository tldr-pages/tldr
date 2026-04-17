# ibmcloud

> Manage IBM Cloud resources, apps, and services.
> Some subcommands such as `login`, `target`, `iam`, `ks`, and `cr` have their own usage documentation.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli>.

- Log in to IBM Cloud:

`ibmcloud login`

- Log in with a federated ID using SSO:

`ibmcloud login --sso`

- Set the target region and resource group:

`ibmcloud target --region {{region}} --resource-group {{resource_group}}`

- List all resource groups:

`ibmcloud resource groups`

- List all service instances in the current target:

`ibmcloud resource service-instances`

- Update the IBM Cloud CLI:

`ibmcloud update`

- Display help for a subcommand:

`ibmcloud help {{subcommand}}`
