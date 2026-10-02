# crypto

> Beheer cryptografie.
> Toegankelijk in de configuratiemodus.
> Meer informatie: <https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/crypto-is-cz-commands.html>.

- Genereer een `rsa`-sleutel:

`crypto key generate rsa`

- Definieer een modulus voor een sleutel:

`crypto key generate rsa modulus {{1024}}`

- Verwijder alle sleutels:

`crypto key zeroize`
