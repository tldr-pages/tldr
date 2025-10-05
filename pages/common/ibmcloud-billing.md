# ibmcloud billing

> Retrieve usage and billing information for IBM Cloud.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli>.

- View account usage:

`ibmcloud billing account-usage`

- View resource group usage:

`ibmcloud billing resource-group-usage {{resource_group_name}}`

- View organization usage:

`ibmcloud billing org-usage {{org_name}}`

- View resource instances usage:

`ibmcloud billing resource-instances-usage`

- View billing information for a specific month:

`ibmcloud billing account-usage -d {{YYYY-MM}}`
