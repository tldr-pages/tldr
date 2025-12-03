# apx stacks

> Administra stacks en `apx`.
> Nota: las configuraciones de stacks creadas por el usuario se almacenan en `~/.local/share/apx/stacks`.
> Más información: <https://docs.vanillaos.org/docs/en/apx-manpage#stacks>.

- Crea de forma interactiva una nueva configuración de stack:

`apx stacks new`

- Actualiza de forma interactiva una configuración de stack:

`apx stacks update {{nombre}}`

- Muestra la lista de todas las configuraciones de stacks disponibles:

`apx stacks list`

- Elimina una configuración de stack específica:

`apx stacks rm --name {{cadena_de_caracteres}}`

- Importa una configuración de stack:

`apx stacks import --input {{ruta/al/stack.yml}}`

- Exporta una configuración de stack (Nota: la opción de salida es opcional, por defecto se exporta al directorio de trabajo actual):

`apx stacks export --name {{cadena_de_caracteres}} --output {{ruta/al/archivo_de_salida}}`
