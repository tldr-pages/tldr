# az term

> Manage marketplace agreement with marketplaceordering.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/term>.

- Print marketplace terms:

`az term show --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`

- Accept marketplace terms:

`az term accept --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`
