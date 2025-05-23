# oct

> The CLI tool for inspecting, configuring and using
> an OpenPGP card device
> More information: <https://codeberg.org/openpgp-card/openpgp-card-tools>.

- List all currently connected cards:

`oct list`

- Inspect card status

`oct status`

- Generate a key on the card

`oct admin --card "{{card-manufacturer-id}}:{{card-serial-number}}" generate {{rsa2048|rsa3072|rsa4096|nistp256|nistp384|nistp521|curve25510}}`

- Sign a file using a smartcard

`oct sign --card "{{card-vendor-id}}:{{card-serial-number}}" detached "{{input-file}}"`

- Decrypt  a file using a smartcard

`oct decrypt --card "{{card-vendor-id}}:{{card-serial-number}}" "{{input-file}}"`

- Change user pin

`oct pin --card "{{card-vendor-id}}:{{card-serial-number}}" set-user`

- Change admin pin

`oct pin --card "{{card-vendor-id}}:{{card-serial-number}}" set-admin`
