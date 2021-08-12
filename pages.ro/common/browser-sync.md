# browser-sync

> Pornește serverul web local care actualizează browserul pe modificările de fișier.
> Mai multe informaţii: <https://browsersync.io/docs/command-line>

- Porniți un server dintr-un anumit director:

`browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}`

- Porniți un server din directorul local, vizionând toate fișierele css într-un director:

`browser-sync start --server --files '{{path/to/directory/*.css}}'`

- Creează fișierul de configurare:

`browser-sync init`

- Porniți browser-sync din fișierul de configurare:

`browser-sync start --config {{config_file}}`
