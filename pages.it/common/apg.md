# apg

> Crea password randomiche arbitrariamente complesse.
> Maggiori informazioni: <https://manned.org/apg>.

- Genera password randomiche (la lunghezza predefinita è 8):

`apg`

- Crea una password con almeno 1 simbolo (S), 1 numero (N), 1 lettera maiuscola (C) e una minuscola (L):

`apg -M SNCL`

- Crea una password di 16 caratteri:

`apg -m {{16}}`

- Crea una password di massimo 16 caratteri:

`apg -x {{16}}`

- Crea una password che non è già presente in un dizionario (file dizionario fornito come argomento):

`apg -r {{percorso/del/dizionario}}`
