# sops

> SOPS: Secrets OPerationS.
> Simple and flexible tool for managing secrets.
> More information: <https://github.com/mozilla/sops>.

- Encrypt a file:

`sops -e {{path/to/myfile.json}} > {{path/to/myfile.enc.json}}`

- Decrypt a file to the standard output:

`sops -d {{path/to/myfile.enc.json}}`

- Rotate data keys for a sops file:

`sops -r {{path/to/myfile.enc.yaml}}`

- Change the extension of the file once encrypted:

`sops -d --input-type json {{path/to/myfile.enc.json}}`

- Extract keys by naming them, and array elements by numbering them:

`sops -d --extract '["an_array"][1]' {{path/to/myfile.enc.json}}`

- Show the difference between two sops files:

`diff <(sops -d {{path/to/secret1.enc.yaml}}) <(sops -d {{path/to/secret2.enc.yaml}})`
