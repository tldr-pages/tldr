# az term

> Manage marketplace agreement with marketplaceordering.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/en-us/cli/azure/term?view=azure-cli-latest>.

- Print marketplace terms:

`az term show --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`

- Accept marketplace terms:

`az term accept --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`
