# pip hash

> Calcola gli hash degli archivi dei pacchetti per la verifica.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_hash/>.

- Genera l'hash per un file di pacchetto:

`pip hash {{percorso/del/pacchetto.whl}}`

- Genera l'hash utilizzando uno specifico algoritmo:

`pip hash {{[-a|--algorithm]}} {{sha256|sha384|sha512|...}} {{percorso/del/pacchetto.whl}}`

- Genera gli hash per più file:

`pip hash {{percorso/del/pacchetto1.whl percorso/del/pacchetto2.whl ...}}`

- Genera l'hash per un archivio scaricato:

`pip hash {{percorso/del/pacchetto.tar.gz}}`
