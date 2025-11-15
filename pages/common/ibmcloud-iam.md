# ibmcloud iam

> Manage identities and access to resources.
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_commands_iam>.

- List service IDs in an account:

`ibmcloud iam service-ids`

- List all API keys for a service ID:

`ibmcloud iam service-api-keys {{service_id}}`

- Create an API key for a service ID with a description and without confirmation:

`ibmcloud iam service-api-key-create {{api_key_name}} {{service_id}} {{[-d|--description]}} {{description}} {{[-f|--force]}}`

- List all actions available under this command:

`ibmcloud iam help`
