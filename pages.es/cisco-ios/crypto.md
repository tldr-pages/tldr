# crypto

> Administra la criptografía.
> Se accede en modo de configuración.
> Más información: <https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/crypto-is-cz-commands.html>.

- Genera una clave `rsa`:

`crypto key generate rsa`

- Define un módulo para una clave:

`crypto key generate rsa modulus {{1024}}`

- Elimina todas las claves:

`crypto key zeroize`
