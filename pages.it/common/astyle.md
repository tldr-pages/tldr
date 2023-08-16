# astyle

> Indentatore, formattatore e beautifier di codice sorgente per i linguaggi C, C++, C# e Java.
> Quando eseguito, una copia del file originale è creata con l'estensione ".orig" aggiunta come suffisso.
> Maggiori informazioni: <http://astyle.sourceforge.net>.

- Applica lo stile di default di 4 spazi per livello di indentazione e nessun cambiamento alla formattazione:

`astyle {{file_sorgente}}`

- Applica lo stile Java con parentesi graffe aperte sulla stessa riga (attached braces):

`astyle --style=java {{percorso/del/file}}`

- Applica lo stile allman per parantesi graffe su linee separate (broken braces):

`astyle --style=allman {{percorso/del/file}}`

- Applica un'indentazione personalizzata utilizzando spazi. Scegli tra 2 e 20 spazi:

`astyle --indent=spaces={{numero_spazi}} {{percorso/del/file}}`

- Applica un'indentazione personalizzata utilizzando tab. Scegli tra 2 e 20 tab:

`astyle --indent=tab={{numero_tab}} {{percorso/del/file}}`
