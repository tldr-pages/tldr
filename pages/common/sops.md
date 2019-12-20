# sops

> SOPS: Secrets OPerationS.
> Simple and flexible tool for managing secrets.
> More information: <https://github.com/mozilla/sops>.

- Encrypt a file:

`sops -e myfile.json > myfile.enc.json`

- To decrypt a file in a `cat` fashion, use the `-d` flag:

`sops -d myfile.enc.json`

- To rotate data keys for a sops file:

`sops -r example.enc.yaml`

- Change the extension of the file once encrypted:

`sops -d --input-type json myfile.enc.json`

- Extract keys by naming them, and array elements by numbering them:

`sops -d --extract '["an_array"][1]' myfile.enc.json`

- Diff two sops files:

`diff <(sops -d secret1.enc.yaml) <(sops -d secret2.enc.yaml)`
