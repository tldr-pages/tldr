# vaultcmd

> Manage and interact with Windows Credential Manager vaults.
> More information: <https://learn.microsoft.com/windows/security/identity-protection/credential-manager>.

- List all currently loaded vaults and their GUIDs:

`vaultcmd /list`

- List the schema of all supported credential types:

`vaultcmd /listschema`

- List all credentials stored in a specific vault:

`vaultcmd /listcreds:{{vault_name|vault_guid}} /all`

- List the properties of a specific vault:

`vaultcmd /listproperties:{{vault_name|vault_guid}}`

- Add a new credential to a vault:

`vaultcmd /addcreds:{{vault_name|vault_guid}} /credtype:{{schema_guid}} /identity:{{identity}} /authenticator:{{authenticator}} /resource:{{resource}}`

- Delete a credential from a vault:

`vaultcmd /deletecreds:{{vault_name|vault_guid}} /credtype:{{schema_guid}} /identity:{{identity}}`

- Synchronize credentials across vaults:

`vaultcmd /sync`
