# vault

> Un CLI pentru a interacționa cu seiful HashiCorp.
> Mai multe informaţii: <https://www.vaultproject.io/docs/commands>

- Conectați-vă la un server Vault și inițializați un nou magazin de date criptate:

`vault init`

- Desfaceți (deblocați) seiful, furnizând una dintre acțiunile cheie necesare pentru a accesa depozitul de date criptate:

`vault unseal {{key-share-x}}`

- Autentificați clientul CLI împotriva serverului Vault, utilizând un simbol de autentificare:

`vault auth {{authentication_token}}`

- Păstrați un nou secret în seif, folosind back-end generic numit „secret”:

`vault write secret/{{hello}} value={{world}}`

- Citiți o valoare din seif, folosind back-end generic numit „secret”:

`vault read secret/{{hello}}`

- Citiți un anumit câmp din valoarea:

`vault read -field={{field_name}} secret/{{hello}}`

- Sigilați (blocați) serverul Vault, eliminând cheia de criptare a depozitului de date din memorie:

`vault seal`
