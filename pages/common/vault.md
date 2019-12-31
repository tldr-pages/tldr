# vault

> A CLI to interact with HashiCorp Vault.
> More information: <https://www.vaultproject.io/docs/commands>.

- Connect to a Vault server and initialize a new encrypted data store:

`vault init`

- Unseal (unlock) the vault, by providing one of the key shares needed to access the encrypted data store:

`vault unseal {{key-share-x}}`

- Authenticate the CLI client against the Vault server, using an authentication token:

`vault auth {{authentication_token}}`

- Store a new secret in the vault, using the generic back-end called "secret":

`vault write secret/{{hello}} value={{world}}`

- Read a value from the vault, using the generic back-end called "secret":

`vault read secret/{{hello}}`

- Seal (lock) the Vault server, by removing the encryption key of the data store from memory:

`vault seal`
