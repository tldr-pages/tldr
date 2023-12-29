# blender

> Interfaccia da linea di comando per il programma di grafica Blender 3D.
> Gli argomenti sono eseguiti nell'ordine in cui sono dati.
> Maggiori informazioni: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- Renderizza tutti i frame di una animazione in background, senza caricare l'interfaccia grafica (l'output è salvato in `/tmp`):

`blender --background {{nome_file}}.blend --render-anim`

- Renderizza un'animazione usando uno specifico pattern, in un percorso relativo (`//`) al file `.blend`:

`blender --background {{nome_file}}.blend --render-output //{{render/frame_###.png}} --render-anim`

- Renderizza il decimo frame di un'animazione come singola immagine, salvandolo in una directory esistente (percorso assoluto):

`blender --background {{nome_file}}.blend --render-output {{/percorso/della/directory_output}} --render-frame {{10}}`

- Renderizza il penultimo frame di un'animazione come immagine JPEG, salvandolo in una directory esistente (path relativa al file):

`blender --background {{nome_file}}.blend --render-output //{{directory_output}} --render-frame {{JPEG}} --render-frame {{-2}}`

- Renderizza l'animazione di una specifica scena, dal frame 10 al 500:

`blender --background {{nome_file}}.blend --scene {{nome_scena}} --frame-start {{10}} --frame-end {{500}} --render-anim`

- Renderizza un'animazione ad una specifica risoluzione, attraverso l'utilizzo di uno script python:

`blender --background {{nome_file}}.blend --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' --render-anim`

- Avvia una sessione interattiva di Blender nel terminale con una console python (esegui `import bpy` dopo l'avvio):

`blender --background --python-console`
