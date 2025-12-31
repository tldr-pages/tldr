# exo iam

> Manage the Exoscale IAM service.
> More information: <https://community.exoscale.com/product/iam/>.

- List all of the IAM roles:

`exo iam role list`

- Create a new API key:

`exo iam api-key create {{api_key_name}} {{iam_role_name}}`

- Create a new IAM role:

`cat {{path/to/policy.json}} | exo iam role create {{iam_role_name}} --editable --policy -`

- Show the policy of an existing IAM role:

`exo iam role show {{iam_role_name}} --policy {{[-O|--output-format]}} {{json}} | jq .`

- Update the default Organization policy (the default Organization policy will be applied to all of the API keys within the Organization):

`cat {{path/to/policy.json}} | exo iam org-policy update -`
