# script

> Înregistrați toate ieșirile terminale în fișier.

- Înregistrați o nouă sesiune într-un fișier denumit `typescript' în directorul curent:

`script`

- Înregistrați o nouă sesiune într-un fișier particularizat:

`script {{path/to/session.out}}`

- Înregistrați o sesiune nouă, anexând la un fișier existent:

`script -a {{path/to/session.out}}`

- Informații de sincronizare a înregistrării (datele sunt transmise la eroarea standard):

`script -t 2> {{path/to/timingfile}}`
