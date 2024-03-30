# ar

> Crea, modifica ed estrai da archivi (`.a`, `.so`, `.o`).
> Maggiori informazioni: <https://manned.org/ar>.

- Estrai ([x]) tutti i membri da un archivio:

`ar x {{percorso/del/file.a}}`

- Lis[t]a tutti i membri di un archivio:

`ar t {{percorso/del/file.ar}}`

- Sostituisci ([r]) o aggiungi file ad un archvio:

`ar r {{percorso/del/file.deb}} {{percorso/del/debian-binary percorso/del/control.tar.gz percorso/del/data.tar.xz ...}}`

- In[s]erisci o sostituisci un indice in un archivio (equivalente ad usare `ranlib`):

`ar s {{percorso/del/file.a}}`

- Crea un archivio con dei file creando anche il relativo indice:

`ar rs {{percorso/del/file.a}} {{percorso/del/file1.o percorso/del/file2.o ...}}`
