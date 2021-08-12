# snapper

> Instrument de gestionare instantanee a sistemului de fișiere.
> Mai multe informaţii: <http://snapper.io/manpages/snapper.html>

- Configs instantaneu listă:

`snapper list-configs`

- Creați configurare snapper:

`snapper -c {{config}} create-config {{path/to/directory}}`

- Creați un instantaneu cu o descriere:

`snapper -c {{config}} create -d "{{snapshot_description}}"`

- Listează instantanee pentru o configurare:

`snapper -c {{config}} list`

- Şterge un instantaneu:

`snapper -c {{config}} delete {{snapshot_number}}`

- Ștergeți o gamă de instantanee:

`snapper -c {{config}} delete {{snapshot_X}}-{{snapshot_Y}}`
