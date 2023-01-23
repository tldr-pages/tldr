# vault

> CLI a HashiCorp Vault-tal való interakcióhoz. További információ: <https://www.vaultproject.io/docs/commands>.

- Csatlakozás egy Vault-kiszolgálóhoz és egy új titkosított adattároló inicializálása:

`vault init`

- A páncélterem feloldása (feloldása) a titkosított adattároló eléréséhez szükséges kulcsmegosztások egyikének megadásával:

`vault unseal {{key-share-x}}`

- Hitelesítse a CLI-ügyfelet a Vault-kiszolgálóval szemben egy hitelesítési token segítségével:

`vault auth {{authentication_token}}`

- Új titok tárolása a páncélteremben a "secret" nevű általános háttértár használatával:

`vault write secret/{{hello}} value={{world}}`

- Egy érték kiolvasása a páncélteremből a "secret" nevű általános háttértár segítségével:

`vault read secret/{{hello}}`

- Egy adott mező kiolvasása az értékből:

`vault read -field={{field_name}} secret/{{hello}}`

- A páncélterem-kiszolgáló lezárása (zárolása) az adattároló titkosítási kulcsának a memóriából való eltávolításával:

`vault seal`
