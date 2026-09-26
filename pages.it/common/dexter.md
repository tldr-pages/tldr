# dexter

> Strumento per autenticare utenti kubectl con OpenId Connect.
> Maggiori informazioni: <https://github.com/gini/dexter#run-dexter>.

- Crea ed autentica un utente con Google OIDC:

`dexter auth {{[-i|--client-id]}} {{id_client}} {{[-s|--client-secret]}} {{segreto_client}}`

- Sovrascrivi la posizione predefinita della configurazione di kube:

`dexter auth {{[-i|--client-id]}} {{id_client}} {{[-s|--client-secret]}} {{segreto_client}} {{[-k|--kube-config]}} {{percorso/della/configurazione}}`
