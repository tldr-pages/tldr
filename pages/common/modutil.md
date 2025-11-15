# modutil

> Manage PKCS #11 module information within the NSS security module database.
> More information: <https://manned.org/modutil>.

- Add a PKCS #11 module to a NSS database (e.g. a Firefox profile: `$HOME/.mozilla/firefox/default-release`):

`modutil -dbdir sql:{{path/to/nss_database_directory}} -add "{{module_label}}" -libfile {{path/to/pkcs11_mod.so}}`

- List PKCS #11 modules in a NSS database:

`modutil -dbdir sql:{{path/to/nss_database_directory}} -list`
