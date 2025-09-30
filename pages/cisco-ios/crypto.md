# crypto

> Manage cryptography.
> Accessed in configuration mode.
> More information: <https://www.cisco.com/c/en/us/td/docs/security/asa/asa-cli-reference/A-H/asa-command-ref-A-H/crypto-is-cz-commands.html>.

- Generate an `rsa` key:

`crypto key generate rsa`

- Define a modulus for a key:

`crypto key generate rsa modulus {{1024}}`

- Remove all keys:

`crypto key zeroize`
