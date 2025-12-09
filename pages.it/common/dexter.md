# dexter

> Strumento per autenticare utenti kubectl con OpenId Connect.
> Maggiori informazioni: <https://github.com/gini/dexter>.

- Crea ed autentica un utente con Google OIDC:

`dexter auth -i {{id-client}} -s {{segreto-client}}`

- Sovrascrivi la posizione predefinita della configurazione di kube:

`dexter auth -i {{id-client}} -s {{segreto-client}} --kube-config {{percorso/della/configurazione}}`
