# dexter

> Instrument pentru autentificarea utilizatorilor kubectl cu OpenID Connect.
> Mai multe informaţii: <https://github.com/gini/dexter>

- Creați și autentificați un utilizator cu Google OIDC:

`dexter auth -i {{client_id}} -s {{client_secret}}`

- Suprascrie locația implicită a configurării kube:

`dexter auth -i {{client_id}} -s {{client_secret}} --kube-config {{sample/config}}`
