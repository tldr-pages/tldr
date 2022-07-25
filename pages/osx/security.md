# security

> Administer Keychains, keys, certificates and the Security framework.
> More information: <https://ss64.com/osx/security.html>.

- List the available keychains:

`security list-keychains`

- Delete a specific keychain:

`security delete-keychain {{path}}`

- Create a keychain:

`security create-keychain -p {{password}} {{keychain.name}}`

- Set a certificate to use with a website or [s]ervice by its [c]ommon name (fails if several certificates with the same common name exist):

`security set-identity-preference -s {{URL|hostname|service}} -c "{{common_name}}" {{path/to/file.keychain}}`

- Add a certificate from file to a [k]eychain (if -k isn't specified, the default keychain is used):

`security add-certificates -k {{keychain.name}} {{path/to/file.pem}}`

- Add a CA certificate to the per-user Trust Settings:

`security add-trusted-cert -k {{path/to/login.keychain-db}} {{ca-cert.pem}}`

- Remove a CA certificate from the per-user Trust Settings:

`security remove-trusted-cert -d {{ca-cert.pem}}`
