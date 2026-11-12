# aspell

> Correttore ortografico interattivo.
> Maggiori informazioni: <http://aspell.net/man-html/index.html>.

- Controllare l'ortografia di un singolo file:

`aspell check {{percorso/del/file}}`

- Elencare le parole errate da `stdin`:

`cat {{percorso/del/file}} | aspell list`

- Mostrare i dizionari linguistici disponibili:

`aspell dicts`

- Eseguire `aspell` con una lingua diversa (accetta il codice linguistico ISO 639 a due lettere):

`aspell --lang {{cs}}`

- Elencare le parole errate da `stdin` e ignorare le parole presenti nella lista personale:

`cat {{percorso/del/file}} | aspell --personal {{lista_parole_personali.pws}} list`
