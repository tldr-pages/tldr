# security

> Administer Keychains, keys, certificates and the Security framework.
> More information: <https://ss64.com/osx/security.html>.

- List the available keychains:

`security list-keychains`

- Delete a specific keychain:

`security delete-keychain {{path}}`

- Create a keychain:

`security create-keychain -p {{password}} {{keychain.name}}`

- Set a preferred certificate to use with a website or [s]ervice by its [c]ommon name. Note that this will fail if several certificates with the same common name exist.

`security set-identity-preference -s {{URL, hostname, or service}} -c {{friendly certificate name in keychain}} {{path such as /Library/Keychains/System.keychain}}`

- Add a certificate from file to a [k]eychain, if -k not specified the default keychain is used

`security add-certificates [-k {{keychain.name}}] {{path}}`