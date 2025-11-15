# sops

> SOPS (Secrets OPerationS): a simple and flexible tool for managing secrets.
> More information: <https://github.com/getsops/sops>.

- Encrypt a file:

`sops -e {{path/to/file.json}} > {{path/to/file.enc.json}}`

- Decrypt a file to `stdout`:

`sops -d {{path/to/file.enc.json}}`

- Update the declared keys in a `sops` file:

`sops updatekeys {{path/to/file.enc.yaml}}`

- Rotate data keys for a `sops` file:

`sops -r {{path/to/file.enc.yaml}}`

- Change the extension of the file once encrypted:

`sops -d --input-type json {{path/to/file.enc.json}}`

- Extract keys by naming them, and array elements by numbering them:

`sops -d --extract '["an_array"][1]' {{path/to/file.enc.json}}`

- Show the difference between two `sops` files:

`diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})`
