# blender

> Interfaccia da linea di comando per il programma di grafica Blender 3D.
> Gli argomenti sono eseguiti nell'ordine in cui sono dati.
> Maggiori informazioni: <https://manned.org/blender>.

- Renderizza tutti i frame di una animazione in background, senza caricare l'interfaccia grafica (l'output è salvato in `/tmp`):

`blender -b {{nome_file}}.blend -a`

- Renderizza un'animazione usando uno specifico pattern, in un percorso relativo (`//`) al file `.blend`:

`blender -b {{nome_file}}.blend -o //{{render/frame_###.png}} -a`

- Renderizza il decimo frame di un'animazione come singola immagine, salvandolo in una directory esistente (percorso assoluto):

`blender -b {{nome_file}}.blend -o {{/percorso/della/directory_output}} -f {{10}}`

- Renderizza il penultimo frame di un'animazione come immagine JPEG, salvandolo in una directory esistente (path relativa al file):

`blender -b {{nome_file}}.blend -o //{{directory_output}} -F {{JPEG}} -f {{-2}}`

- Renderizza l'animazione di una specifica scena, dal frame 10 al 500:

`blender -b {{nome_file}}.blend -S {{nome_scena}} -s {{10}} -e {{500}} -a`

- Renderizza un'animazione ad una specifica risoluzione, attraverso l'utilizzo di uno script python:

`blender -b {{nome_file}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' -a`

- Avvia una sessione interattiva di Blender nel terminale con una console python (esegui `import bpy` dopo l'avvio):

`blender -b --python-console`
