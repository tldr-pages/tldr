# ibmcloud target

> Set or view the target account, region, or resource group.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target>.

- View the current target account and region:

`ibmcloud target`

- Set the target account:

`ibmcloud target -c {{account_id}}`

- Switch to a specific region:

`ibmcloud target -r {{region_name}}`

- Set the target resource group:

`ibmcloud target -g {{resource_group_name}}`

- Clear the targeted region:

`ibmcloud target --unset-region`

- Clear the targeted resource group:

`ibmcloud target --unset-resource-group`
