# security

> Administer keychains, keys, certificates and the Security framework.
> More information: <https://keith.github.io/xcode-man-pages/security.1.html>.

- List all available keychains:

`security list-keychains`

- Delete a specific keychain:

`security delete-keychain {{path/to/file.keychain}}`

- Create a keychain:

`security create-keychain -p {{password}} {{path/to/file.keychain}}`

- Set a certificate to use with a website or [s]ervice by its [c]ommon name (fails if several certificates with the same common name exist):

`security set-identity-preference -s {{URL|hostname|service}} -c "{{common_name}}" {{path/to/file.keychain}}`

- Add a certificate from file to a [k]eychain (if -k isn't specified, the default keychain is used):

`security add-certificates -k {{file.keychain}} {{path/to/cert_file.pem}}`

- Add a CA certificate to the per-user Trust Settings:

`security add-trusted-cert -k {{path/to/user-keychain.keychain-db}} {{path/to/ca-cert_file.pem}}`

- Remove a CA certificate from the per-user Trust Settings:

`security remove-trusted-cert {{path/to/ca-cert_file.pem}}`
