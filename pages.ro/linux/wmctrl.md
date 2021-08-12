# wmctrl

> CLI pentru X Window Manager.

- Listează toate ferestrele, gestionate de managerul de ferestre:

`wmctrl -l`

- Treceți la prima fereastră a cărei (parțială) titlu se potrivește:

`wmctrl -a {{window_title}}`

- Mutați o fereastră în spațiul de lucru curent, ridicați-o și dați-i focalizare:

`wmctrl -R {{window_title}}`

- Treceți la un spațiu de lucru:

`wmctrl -s {{workspace_number}}`

- Selectați o fereastră și comutați ecranul complet:

`wmctrl -r {{window_title}} -b toggle,fullscreen`

- Selectați o fereastră o mutați-l într-un spațiu de lucru:

`wmctrl -r {{window_title}} -t {{workspace_number}}`
