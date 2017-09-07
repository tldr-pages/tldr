# vault

> A CLI to interact with HashiCorp Vault.

- Create a new vault, requiring at least 2 out of 5 keyshares to unseal:

`vault init -key-shares={{5}} -key-threshold={{2}}`

- Unseal the vault:

`vault unseal {{key-share-x}}`

- Authenticate client against vault, using an authentication token:

`vault auth {{authentication-token}}`

- Store a new secret in the vault:

`vault write {{secret/hello}} value={{world}}`

- Read a secret from the vault:

`vault read {{secret/hello}}`

- Seal the vault again:

`vault seal`
