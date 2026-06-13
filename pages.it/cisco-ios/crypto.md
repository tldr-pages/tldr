# crypto

> Gestisce la crittografia.
> Accessibile in modalità configurazione.
> Maggiori informazioni: <https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/crypto-is-cz-commands.html>.

- Genera una chiave `rsa`:

`crypto key generate rsa`

- Definisce un modulo per una chiave:

`crypto key generate rsa modulus {{1024}}`

- Rimuove tutte le chiavi:

`crypto key zeroize`
