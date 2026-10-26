# vaultcmd

> Create, display, and delete credentials stored in Windows Credential Manager vaults.
> See also: `cmdkey`.
> More information: <https://support.microsoft.com/windows/security/credential-manager-in-windows>.

- List the loaded vaults:

`vaultcmd /list`

- List credentials in a vault:

`vaultcmd /listcreds:"{{vault_name}}"`

- Show how many credentials a vault holds and how they are protected:

`vaultcmd /listproperties:"{{vault_name}}"`

- Show the syntax for adding a credential, including the schema GUID to pass to `/credtype`:

`vaultcmd /addcreds /?`

- Add a credential:

`vaultcmd /addcreds:"{{vault_name}}" /credtype:{{schema_guid}} /identity:{{username}} /authenticator:{{password}} /resource:{{resource}} /savedBy:{{username}}`

- Delete a credential:

`vaultcmd /deletecreds:"{{vault_name}}" /credtype:{{schema_guid}} /identity:{{username}} /resource:{{resource}} /sid:{{package_sid}}`

- Display help:

`vaultcmd /?`
