# blender

> Interfaccia da linea di comando per il programma di grafica Blender 3D.
> Gli argomenti sono eseguiti nell'ordine in cui sono dati.
> Maggiori informazioni: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- Renderizza tutti i frame di una animazione in background, senza caricare l'interfaccia grafica (l'output è salvato in `/tmp`):

`blender {{[-b|--background]}} {{nome_file.blend}} {{[-a|--render-anim]}}`

- Renderizza un'animazione usando uno specifico pattern, in un percorso relativo (`//`) al file `.blend`:

`blender {{[-b|--background]}} {{nome_file.blend}} {{[-o|--render-output]}} //{{render/frame_###.png}} {{[-a|--render-anim]}}`

- Renderizza il decimo frame di un'animazione come singola immagine, salvandolo in una directory esistente (percorso assoluto):

`blender {{[-b|--background]}} {{nome_file.blend}} {{[-o|--render-output]}} /{{percorso/della/directory_output}} {{[-f|--render-frame]}} {{10}}`

- Renderizza il penultimo frame di un'animazione come immagine JPEG, salvandolo in una directory esistente (path relativa al file):

`blender {{[-b|--background]}} {{nome_file.blend}} {{[-o|--render-output]}} //{{directory_output}} {{[-f|--render-frame]}} {{JPEG}} {{[-f|--render-frame]}} {{-2}}`

- Renderizza l'animazione di una specifica scena, dal frame 10 al 500:

`blender {{[-b|--background]}} {{nome_file.blend}} {{[-S|--scene]}} {{nome_scena}} {{[-s|--frame-start]}} {{10}} {{[-e|--frame-end]}} {{500}} {{[-a|--render-anim]}}`

- Renderizza un'animazione ad una specifica risoluzione, attraverso l'utilizzo di uno script python:

`blender {{[-b|--background]}} {{nome_file.blend}} --python-expr '{{import bpy; bpy.data.scenes[0].render.resolution_percentage = 25}}' {{[-a|--render-anim]}}`

- Avvia una sessione interattiva di Blender nel terminale con una console python (esegui `import bpy` dopo l'avvio):

`blender {{[-b|--background]}} --python-console`
