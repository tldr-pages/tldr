# chpasswd

> Cambia le password di più utenti utilizzando `stdin`.
> Maggiori informazioni: <https://manned.org/chpasswd.8>.

- Cambia la password di un utente specifico:

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- Cambia le password di più utenti (il testo in input non deve contenere spazi):

`printf "{{username_1}}:{{new_password_1}}\n{{username_2}}:{{new_password_2}}" | sudo chpasswd`

- Cambia la password di un utente specifico, specificandola in forma crittografata:

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd --encrypted`

- Cambia la password di un utente specifico e utilizza un metodo di crittografia specifico:

`printf "{{username}}:{{new_password}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}`
