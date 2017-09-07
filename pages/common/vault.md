# vault

> HashiCorp Vault, a tool for managing secrets.

- Create a new vault, requiring at least 2 out of 5 keyshares to unseal:

`vault init -key-shares={{5}} -key-threshold={{2}}`

- Unseal a vault, by providing one of the keyshares. Repeat with necessary key-shares until unsealed:

`vault unseal {{key-share-x}}`

- Authenticate client against vault, using an authentication token:

`vault auth {{authentication-token}}`

- Store a new secret in the vault:

`vault write {{secret/hello}} value={{world}}`

- Read a secret from the vault:

`vault read {{secret/hello}}`

- Seal the vault:

`vault seal`
