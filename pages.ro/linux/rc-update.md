# rc-update

> Adăugați și eliminați serviciile OpenRC la și de la nivelurile de execuție.
> A se vedea, de asemenea, `openrc`.

- Listează toate serviciile și nivelurile de execuție la care sunt adăugate:

`rc-update show`

- Adăugați un serviciu la un nivel de execuție:

`sudo rc-update add {{service_name}} {{runlevel}}`

- Ștergeți un serviciu de la un nivel de execuție:

`sudo rc-update delete {{service_name}} {{runlevel}}`

- Ștergeți un serviciu din toate nivelurile de execuție:

`sudo rc-update --all delete {{service_name}}`
